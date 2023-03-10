import requests
from bs4 import BeautifulSoup
import lxml
from flask import Flask, jsonify, request


def FetchGen(word):
    try:
        url = f'https://en.wiktionary.org/wiki/{word}'

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')

        wordForms = soup.find('span', class_="mw-headline", id="Scottish_Gaelic").findNext("strong").findParent('p')


        if wordForms.find('i', string='genitive singular'):
            gen = wordForms.find('i', string="genitive singular").findNext('b').string

        elif  wordForms.find('i', string='genitive'):
            gen = wordForms.find('i', string="genitive").findNext('b').string

        decodedWord = wordForms.find('strong').string

        return ({
            'status': 200,
            'word': decodedWord,
            'genitive': gen
        })


    except:
        return ({
            'status': 400,
            'message': "word not found"}
        )
