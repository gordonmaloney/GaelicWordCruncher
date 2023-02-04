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
    return('API running - woohoo\n\nroutes:\n/gender\n/ipa\n/audio\n/all' )


@app.route('/gender', methods=['POST'])
def genderroute():
    word = request.form.get('word')
    return gender.FetchGender(word)


@app.route('/ipa', methods=['POST'])
def iparoute():
    word = request.form.get('word')
    return ipa.FetchIpa(word)


@app.route('/audio', methods=['POST'])
def audioroute():
    word = request.form.get('word')
    return audio.FetchAudio(word)


@app.route('/all', methods=['POST'])
def allroutes():
    word = request.form.get('word')
    return jsonify(
        word = word,
        gender = gender.FetchGender(word),
        audio = audio.FetchAudio(word),
        ipa = ipa.FetchIpa(word)
    )


if __name__ == '__main__':
    app.run(port=3252)