import requests
from bs4 import BeautifulSoup
import lxml
from flask import Flask, jsonify, request
from flask_cors import CORS

import gender
import ipa
import audio

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return('API running - routes: /gender/{word}, /ipa/{word}, /audio/{word}, /all/{word}' )


@app.route('/gender/<word>', methods=['GET'])
def genderroute(word):
    return gender.FetchGender(word)


@app.route('/ipa/<word>', methods=['GET'])
def iparoute(word):
    return ipa.FetchIpa(word)


@app.route('/audio/<word>', methods=['GET'])
def audioroute(word):
    return audio.FetchAudio(word)


@app.route('/all/<word>', methods=['GET'])
def allroutes(word):
    return jsonify(
        gender = gender.FetchGender(word),
        audio = audio.FetchAudio(word),
        ipa = ipa.FetchIpa(word)
    )


if __name__ == '__main__':
    app.run(port=3252)