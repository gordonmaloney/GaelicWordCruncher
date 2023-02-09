import requests
from bs4 import BeautifulSoup
import lxml
from flask import Flask, jsonify, request


def FetchAll(word):
    try:
        url = f'https://en.wiktionary.org/wiki/{word}'

        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'lxml')

        ##ipa
        ipa = soup.find("span", id='Scottish_Gaelic').findNext('span', class_='IPA').string


        wordForms = soup.find('span', class_="mw-headline", id="Scottish_Gaelic").findNext("strong").findParent('p')
        decodedWord = wordForms.find('strong').string

        ##gen
        if wordForms.find('i', string='genitive singular'):
            gen = wordForms.find('i', string="genitive singular").findNext('b').string

        elif  wordForms.find('i', string='genitive'):
            gen = wordForms.find('i', string="genitive").findNext('b').string

        ##plur
        plur = wordForms.find('i', string="plural").findNext('b').string


        return ({
            'status': 200,
            'word': decodedWord,
            'genitive': gen,
            'plural': plur,
            'ipa': ipa
        })

    except:
        return ({
            'status': 400,
            'message': "word not found"}
        )

print (FetchAll('clach'))