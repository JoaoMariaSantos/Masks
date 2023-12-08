import requests
from io import BytesIO
from PIL import Image

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


#from https://jsbin.com/gogagosufe/edit?css,js,console,output
def getEmojiCode(emojiText): 
    code = ''
    index = 0
    for char in emojiText:
        if index > 0:
            code += '_'

        base = ord(char)
        base = format(base, 'x')
        base.zfill(4)

        code += base

        index += 1

    return code

emojiSVGLink = "https://emojiapi.dev/api/v1/CODE.svg"
emojiPNGLink = "https://emojiapi.dev/api/v1/CODE/SIZE.png"

def getEmojiSVGLink(emojiCode: str):
    return emojiSVGLink.replace("CODE", emojiCode)

def getEmojiSVGText(emojiCode):
    url = getEmojiSVGLink(emojiCode)
    text = requests.get(url).text
    return text

def saveEmojisPNG(emojis, path, size):
    index = 0
    for e in emojis:
        name = str(index) + ".png"
        url = emojiPNGLink
        url = url.replace("CODE", e["emoji_code"])
        url = url.replace("SIZE", str(size))

        response = requests.get(url, stream=True)

        img = Image.open(response.raw)
        img.save(path + "/" + name)
        index += 1