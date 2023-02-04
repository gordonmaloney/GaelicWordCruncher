import requests
from bs4 import BeautifulSoup
import lxml
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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


def FetchGender(word):
    print('fetching: ' + word)

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
            return jsonify(
                word=FemWord(word),
                gender='fem',
                status=200
            )
        if masculine:
            return jsonify(
                word=MascWord(word),
                gender='masc',
                status=200
            )
    except:
        return jsonify(
            status=404,
            msg='word not found :('
        )


@app.route('/', methods=['GET'])
def home():
    return('welcome to ARTICLISER - add a word to this url to search for it: ' + request.url_root + 'api/' )


@app.route('/api/<word>', methods=['GET'])
def index(word):
    return FetchGender(word)


if __name__ == '__main__':
    app.run(port=3252)