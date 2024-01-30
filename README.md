# Incognito Stickers

Anti Face Recognition stickers generator (WIP).

# About

Website tool that creates a set of stickers unique to each person. 
These stickers, when applied to the user's face, should prevent Facial Recognition systems form recognizing the person.
Input a photo of your face and a text prompt to generate your own unique set of stickers.
Generation created using Genetic Algorithm and [DeepFace](https://github.com/serengil/deepface).

# Getting Started

**Prerequisites**

[OpenAI](https://openai.com) key, required to fetch emojis.

[Python](https://www.python.org/downloads/)

[NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

**Installing**

[OpenAI](https://openai.com) — 
`pip install openai package==0.28.0`     

[DeepFace](https://github.com/serengil/deepface) — 
`pip install deepface`

[Flask](https://pypi.org/project/Flask/) — 
`pip install flask`

[Flask-CORS](https://pypi.org/project/Flask-Cors/) — 
`pip install flask-cors`

[jsonlines](https://pypi.org/project/jsonlines/) — 
`pip install jsonlines`

[numpy](https://numpy.org/install/) — 
`pip install numpy`

[requests](https://pypi.org/project/requests/) — 
`pip install requests`

[Spire.PDF](https://pypi.org/project/Spire.Pdf/) — 
`pip install Spire.PDF`

# Usage

Inside *flask-server, static, secret* directory create openAIKey.txt file. Inside paste your [OpenAI](https://openai.com) key. 

In terminal go to *flask-server* directory and run `python server.py`
In terminal go to *client* directory and run `npm start`

Use in browser.

If any bug arises:

* reset server by pressing *CTRL-C* in terminal where server is running;
* in terminal go to *flask-server* directory and run `python server.py`;
* refresh browser window.

# Credits

**Designer & Developer**

* [João Maria Santos](https://github.com/JoaoMariaSantos)

**Supervisors**

* João Cunha

* Sérgio M. Rebelo

* Pedro Silva

* Penousal Machado

* Tiago Martins

**Emoji Fetching Code**

* lilianweng's [emoji-semantic-search](https://github.com/lilianweng/emoji-semantic-search)
