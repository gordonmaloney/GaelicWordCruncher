import requests
from bs4 import BeautifulSoup
import lxml
from flask import Flask, jsonify, request
from flask_cors import CORS

import gender
import ipa
import audio
import plural
import genitive


def genderroute():
    data = request.get_json()

    word = data['word']
    if word:
        return gender.FetchGender(word)
    else:
        return jsonify(message = 'uh oh')


def iparoute():
    data = request.get_json()
    word = data['word']

    return ipa.FetchIpa(word)


def audioroute():
    data = request.get_json()
    word = data['word']
    return audio.FetchAudio(word)


def pluralroute():
    data = request.get_json()
    word = data['word']
    return plural.FetchPlural(word)

def genroute(word):
    return genitive.FetchGen(word)


def Fetch(word):
        gender.FetchGender(word),
        audio.FetchAudio(word),
        ipa.FetchIpa(word),
        genitive.FetchGen(word),
        plural.FetchPlural(word)



Fetch('duine')