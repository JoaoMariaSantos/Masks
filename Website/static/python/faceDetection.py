from deepface import DeepFace
from imageOperations import *

def detectFace(imagePath):
    results = DeepFace.extract_faces(imagePath, align=False, enforce_detection = False, grayscale = False)

    n_faces = len(results)

    if n_faces > 1:
        return {
            "nFaces": n_faces,
            "msg": str(n_faces) + " faces detected"
        }
    
    facial_area = results[0]['facial_area']

    if facial_area['w'] == 0 or facial_area['h'] == 0:
        return {
            "nFaces": 0,
            "msg": "No faces detected"
        }
    
    print(results[0]['face'])

    face_image = crop_image(imagePath, facial_area)
    face_image.save(imagePath)

    return {
            "nFaces": 1,
            "msg": "One face detected"
        }