import requests
from bs4 import BeautifulSoup
import lxml
from flask import Flask, jsonify, request


def FemWord(word):
    first = word[0]
    second = word[1]
    rest = word[1:]
    if first in ('b', 'c', 'p', 'g', 'm'):
        return("a' "+first+'h'+rest)
    elif first == 'f':
        return('an '+first+'h'+rest)
    elif first == 's' and second in ('l', 'n', 'r', 'a', 'e', 'i', 'u', 'o', 'à', 'è', 'ì', 'ò', 'ù'):
        return('an t-'+word)
    else:
        return('an '+word)

def MascWord(word):
    first = word[0]
    rest = word[1:]
    if first in ('b', 'm', 'p', 'f'):
        return('am '+word)
    elif first in ('a', 'e', 'i', 'u', 'o', 'à', 'è', 'ì', 'ò', 'ù'):
        return('an t-'+word)
    else:
        return('an '+word)






def FaclairFetchGender(word):
    try:
        url = 'https://faclair.info/'
        headers = {'Content-Type': 'text/html'}
        params = {'txtSearch': word}

        r = requests.post(url, headers=headers, params=params)
        soup = BeautifulSoup(r.content, 'lxml')
        td = soup.find('a', string=word)['href']

        word_url = 'https://faclair.info/' + td
        word_r = requests.get(word_url)
        word_soup = BeautifulSoup(word_r.content, 'lxml')
        feminine = word_soup.find('i', string='boir.')
        masculine = word_soup.find('i', string='fir.')

        if feminine:
            return ({
                'status': 200,
                'word': FemWord(word),
                'gender': 'fem'}
            )
        if masculine:
            return ({
                'status': 200,
                'word': MascWord(word),
                'gender': 'masc',
                }
            )

    except:
        return ({
            'status': 404,
            'message': 'word not found :('}
        )



##wiki
def FetchGender(word):
    try:
        url = f'https://en.wiktionary.org/wiki/{word}'

        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'lxml')

        wordForms = soup.find('span', class_="mw-headline", id="Scottish_Gaelic").findNext("strong").findParent('p')

        decodedWord = wordForms.find('strong').string

        gender = wordForms.find('abbr').string

        if gender == 'f':
            return ({
                'status': 200,
                'word': FemWord(decodedWord),
                'gender': 'fem'}
            )
        if gender == 'm':
            return ({
                'status': 200,
                'word': MascWord(decodedWord),
                'gender': 'masc',
                }
            )

    except:
        return ({
            'status': 404,
            'message': 'word not found :('}
        )