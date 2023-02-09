import requests
from bs4 import BeautifulSoup
import lxml
from flask import Flask, jsonify, request
from flask_cors import CORS
import urllib.parse

import gender
import ipa
import audio
import plural
import genitive
import wikibulk

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return('API running - woohoo\n\nroutes:\n/gender\n/ipa\n/audio\n/all' )


@app.route('/gender', methods=['POST'])
def genderroute():
    data = request.get_json()

    word = data['word']
    if word:
        return gender.FetchGender(word)
    else:
        return jsonify(message = 'uh oh')


@app.route('/ipa', methods=['POST'])
def iparoute():
    data = request.get_json()
    word = data['word']

    return ipa.FetchIpa(word)


@app.route('/audio', methods=['POST'])
def audioroute():
    data = request.get_json()
    word = data['word']
    return audio.FetchAudio(word)


@app.route('/plural', methods=['POST'])
def pluralroute():
    data = request.get_json()
    word = data['word']
    return plural.FetchPlural(word)

@app.route('/genitive', methods=['POST'])
def genroute():
    data = request.get_json()
    word = data['word']
    return genitive.FetchGen(word)


@app.route('/all', methods=['POST'])
def allroutes():
    data = request.get_json()
    word = urllib.parse.quote(data['word'], safe="")
    print(word)
    return jsonify(
        word = data['word'],
        gender = gender.FetchGender(word),
        audio = audio.FetchAudio(data['word']),
        ipaGenPl = wikibulk.FetchAll(word)
    )


if __name__ == '__main__':
    app.run(port=3252)