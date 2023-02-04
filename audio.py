import requests
from bs4 import BeautifulSoup
import json
from flask import Flask, jsonify, request

def FetchAudio(word):
    url = 'https://www.learngaelic.net/dictionary/search'
    headers = {'Content-Type': 'text/html'}
    params = {'abairt': word}

    try:
        r = requests.post(url, headers=headers, params=params)

        soup = BeautifulSoup(r.content, 'lxml')
        id = soup.find('p')
        string = str(id.text)

        # convert to json
        json_object = json.loads(string)

        word_id = json_object[0]['id']

        mp3_url = f'https://s3-eu-west-1.amazonaws.com/lg-dic/{word_id}.mp3'

        return ({
            'status': 200,
            'file': mp3_url}
        )

    except:
        return ({
            'status': 400,
            'message': "word not found"}
        )