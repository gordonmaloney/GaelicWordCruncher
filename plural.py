import requests
from bs4 import BeautifulSoup
import lxml
from flask import Flask, jsonify, request


def FetchPlural(word):
    try:
        url = f'https://en.wiktionary.org/wiki/{word}'

        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'lxml')

        wordForms = soup.find('span', class_="mw-headline", id="Scottish_Gaelic").findNext("strong", string=word).findParent('p')

        plur = wordForms.find('i', string="plural").findNext('b').string

        return ({
            'status': 200,
            'word': word,
            'plural': plur
        })

    except:

        return ({
            'status': 400,
            'message': "word not found"}
        )


print(FetchPlural('duine'))