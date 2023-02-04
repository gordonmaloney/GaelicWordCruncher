import requests
from bs4 import BeautifulSoup
import lxml
from flask import Flask, jsonify, request


def FetchIpa(word):
    try:
        ipa_url = f'https://en.wiktionary.org/wiki/{word}'

        r_ipa = requests.get(ipa_url)

        soup_ipa = BeautifulSoup(r_ipa.content, 'lxml')

        ipa = soup_ipa.find("span", id='Scottish_Gaelic').findNext('span', class_='IPA').string

        return ({
            'status': 200,
            'word': word,
            'ipa': ipa
        })

    except:
        return ({
            'status': 400,
            'message': "word not found"}
        )