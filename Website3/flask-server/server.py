import os
from flask import Flask, request, send_file
from flask_cors import CORS
from faceDetection import *

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
        return {"msg": ["no image"]}
    
    file = request.files['face']
    
    if file.filename == '':
        return {"msg": ["no name"]}
    
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        detection = detectFace(filename)
        if detection['nFaces'] < 1:
            return {"msg": ["no face detected"]}
        elif detection['nFaces'] > 1:
            return {"msg": ["more than one face detected"]}
        else:
            return {"msg": ["nice"]}

def initServer():
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

if __name__ == "__main__":
    app.run(debug = True)

initServer()