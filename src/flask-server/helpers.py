import requests
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from static.evolution.common import *
from static.evolution.evolution import *

from spire.pdf.common import *
from spire.pdf import *

from faceDetection import *

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

        try:
            img = Image.open(response.raw)
            img.save(path + "/" + name)
        except UnidentifiedImageError as e:
            print("error fetching from: " + url)

        index += 1

def createExportPdf():
    #https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Image/Python-Add-Replace-or-Remove-Images-in-a-PDF-Document.html#:~:text=Replace%20an%20Image%20in%20a%20PDF%20Document%20in%20Python,-Spire.&text=PDF%20for%20Python%20offers%20the,ReplaceImage()%20method.

    doc = PdfDocument()

    pdfPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'pdf', 'exportTemplatePDF.pdf')

    doc.LoadFromFile(pdfPath)

    page = doc.Pages[0]

    imgPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'evolution','individuals', '0', 'img.jpeg')

    image = PdfImage.FromFile(imgPath)

    imageHelper = PdfImageHelper()

    imageInfo = imageHelper.GetImagesInfo(page)

    imageHelper.ReplaceImage(imageInfo[0], image)

    doc.SaveToFile("static/pdf/exportPDF.pdf", FileFormat.PDF)
