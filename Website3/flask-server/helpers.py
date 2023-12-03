from faceDetection import *
from static.evolution.evolution import *

#gets chatgpt key from text file
def getOpenAIKey():
    file_path = 'static/secret/openAIKey.txt'

    try:
        with open(file_path, 'r') as file:
            secret_key = file.read().strip()
        return secret_key
    except FileNotFoundError:
        return ''
    except Exception as e:
        return ''