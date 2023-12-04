import os
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import helpers
import openai

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    clearUploads()

    #upload image to uploads folder
    if 'face' not in request.files:
        return {"error": ["no image"]}
    
    file = request.files['face']
    
    if file.filename == '':
        return {"error": ["no name"]}
    
    if file:
        helpers.setFaceFilename(file.filename)
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        detection = helpers.detectFace(filename)
        if detection['nFaces'] < 1:
            return {"error": ["No face detected"]}
        elif detection['nFaces'] > 1:
            return {"error": ["More than one face detected"]}
        else:
            return {"error": [""]}

@app.route("/chosenEmojis", methods=['POST'])
def getChosenEmojis():
    data = request.get_json()
    prompt = data.get('prompt')

    key = helpers.getOpenAIKey()

    if key == '': 
        return {"msg": ["error"]}
    
    #FREE CHATGPT API -> https://github.com/ayaka14732/ChatGPTAPIFree
    openai.api_key = key
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Your reply will contain only 5 emojis and nothing else."},
            {"role": "user", "content": "Generate 5 emojis related to the prompt: \"" + prompt + "\""},
            #{"role": "assistant", "content": "The emojis are related to the given prompt."},
            {"role": "user", "content": "Your answer should only contain the 5 emojis."}
        ],
        max_tokens=50,
        n=1  # Number of options to generate
    )
    print(response)
    emojis = response['choices']
    return jsonify({'emojis': emojis})

@app.route("/startgeneration", methods=['POST'])
def startGeneration():
    print("starting generation")
    helpers.startEvolution()
    return  {"msg": ["nice"]}


def onStartup():
    clearUploads()

def clearUploads():
    #delete images in uploads folder
    for file_name in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error: {e}")

### Runs on startup
with app.app_context():
    onStartup()

if __name__ == "__main__":
    app.run(debug = True)