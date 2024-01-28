import os
import gzip
import requests

import jsonlines
import numpy as np
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
import helpers
import openai

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, threaded=True, cors_allowed_origins="*")

openai.api_key = helpers.getOpenAIKey()
openai.api_base = "https://api.openai.com/v1"
EMBEDDING_MODEL = "text-embedding-ada-002"

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
BEST_INDIVIDUAL_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'evolution','individuals', '0')
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
EMOJI_SVG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'emojis', 'svg')
EMOJI_PNG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'emojis', 'png')

EMBEDDING_MODEL = "text-embedding-ada-002"
SERVER_DIR = os.path.dirname(os.path.abspath(__file__))
EMBED_FILE = os.path.join(SERVER_DIR, "emoji-embeddings.jsonl.gz")

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/uploadedface")
def getUploadedFace():

    for file_name in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        try:
            if os.path.isfile(file_path):
                return send_file(file_path)
        except Exception as e:
            return {"msg": ["no image"]}
    return {"msg": ["no image"]}

@app.route("/uploadface", methods=['POST'])
def uploadPhoto():
    clearDirectory(UPLOAD_FOLDER)

    #upload image to uploads folder
    if 'face' not in request.files:
        return {"error": ["no image"]}
    
    file = request.files['face']
    
    if file.filename == '':
        return {"error": ["no name"]}
    
    if file:
        helpers.setFaceFilename(file.filename)
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        detection = helpers.detectFace(filename)
        if detection['nFaces'] < 1:
            return {"error": ["No face detected"]}
        elif detection['nFaces'] > 1:
            return {"error": ["More than one face detected"]}
        else:
            return {"error": [""]}

class EmojiSearchApp:
    def __init__(self):
        self._emojis = None
        self._embeddings = None

    def _load_emoji_embeddings(self):
        if self._emojis is not None and self._embeddings is not None:
            return

        with gzip.GzipFile(fileobj=open(EMBED_FILE, "rb"), mode="rb") as fin:
            emoji_info = list(jsonlines.Reader(fin))

        print("Lazy loading embedding info ...")
        self._emojis = [(x["emoji"], x["message"]) for x in emoji_info]
        self._embeddings = [x["embed"] for x in emoji_info]
        assert self._emojis is not None and self._embeddings is not None

    @property
    def emojis(self):
        if self._emojis is None:
            self._load_emoji_embeddings()
        return self._emojis

    @property
    def embeddings(self):
        if self._embeddings is None:
            self._load_emoji_embeddings()
        return self._embeddings

    def get_openai_embedding(self, text: str) -> list[float]:
        result = openai.Embedding.create(input=text, model=EMBEDDING_MODEL)
        return result["data"][0]["embedding"]

    def get_top_relevant_emojis(self, query: str, k: int = 20) -> list[dict]:
        query_embed = self.get_openai_embedding(query)
        dotprod = np.matmul(self.embeddings, np.array(query_embed).T)
        m_dotprod = np.median(dotprod)
        ind = np.argpartition(dotprod, -k)[-k:]
        ind = ind[np.argsort(dotprod[ind])][::-1]
        result = [
            {
                "emoji": self.emojis[i][0],
                "emoji_code": helpers.getEmojiCode(self.emojis[i][0]),
                "svg": helpers.getEmojiSVGLink(helpers.getEmojiCode(self.emojis[i][0])),
                "message": self.emojis[i][1].capitalize(),
                "score": (dotprod[i] - m_dotprod) * 100,
            }
            for i in ind
        ]
        return result

@app.route("/chosenEmojis", methods=['POST'])
def getChosenEmojis():
    emoji_search_app = EmojiSearchApp()

    error = None
    result = []

    query = request.get_json().get("query")
    try:
        result = emoji_search_app.get_top_relevant_emojis(query, k=5)
    except Exception as err:
        error = str(err)

    clearDirectory(EMOJI_SVG_DIR)
    clearDirectory(EMOJI_PNG_DIR)
    helpers.saveEmojisPNG(result, EMOJI_PNG_DIR, 72)

    return jsonify(error=error, result=result)

@app.route("/startgeneration", methods=['POST'])
def startGeneration():
    print("starting generation")
    helpers.startEvolution()
    return  {"msg": ["nice"]}

@socketio.on('message_from_server')
def handle_message(message):
    print('Received message:', message)
    # Process message as needed
    socketio.emit('message_to_client', 'Hello from Flask!')

def notifyNewGeneration(distance):
    print("new generation socket notification")
    socketio.emit('new_generation', distance)

@app.route("/bestIndividual")
def getBestIndividual():

    print("getting best individual")

    #if helpers.evolving == False:
    #    return {"msg": ["not evolving"]}

    for file_name in os.listdir(BEST_INDIVIDUAL_FOLDER):
        print(file_name)
        if 'jpeg' not in file_name:
            continue
        file_path = os.path.join(BEST_INDIVIDUAL_FOLDER, file_name)
        try:
            if os.path.isfile(file_path):
                return send_file(file_path)
        except Exception as e:
            return {"msg": ["no image"]}
    return {"msg": ["no image"]}

def onStartup():
    clearDirectory(UPLOAD_FOLDER)
    clearDirectory(EMOJI_SVG_DIR)
    clearDirectory(EMOJI_PNG_DIR)

def clearUploads():
    #delete images in uploads folder
    for file_name in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error: {e}")

def clearDirectory(path):
    print("clearing: " + str(path))
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error: {e}")

### Runs on startup
#with app.app_context():
    #onStartup()

if __name__ == "__main__":
    socketio.run(app, debug=True)
    #app.run(debug = True, threaded=True)