import os
import importlib
from flask import Flask, render_template, request, redirect, url_for

import sys
sys.path.append("static/python")
import faceDetection

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def index():
    delete_uploads()
    return render_template('index.html')

@app.route('/upload_face', methods=['POST'])
def upload_file():

    #delete images in uploads folder
    for file_name in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error: {e}")

    #upload image to uploads folder
    if 'image' not in request.files:
        return render_template('index.html', face_error_message = 'No file')
    
    file = request.files['image']
    
    if file.filename == '':
        return render_template('index.html', face_error_message = 'No file name')
    
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        detection = faceDetection.detectFace(filename)
        if detection['nFaces'] != 1:
            return render_template('index.html', face_error_message = detection['msg'])
        else:
            return render_template('index.html', face_error_message = '', face_img = file.filename)

@app.route('/get_emojis')
def get_emojis():
    print("emojis")
    return render_template('index.html')

@app.route('/start_generating')
def start_generating():
    print("emojis")
    return render_template('index.html')

@app.route('/run_python_script')
def run_python_script():
    # Your Python script logic goes here
    result = "Hello from Python!"
    return render_template('result.html', result=result)

def delete_uploads():
    for file_name in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)