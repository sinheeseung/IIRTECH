import urllib.parse
import urllib.request
import json

opendict_cert_key = 'FCDE6983D27255C93578050A57CEDFF1'


def search_for_words_in_opendict(query):
    # 마지막이 search면 사전 검색 오픈 API, view면 사전 내용 오픈 API입니다.
    defaultURL = 'https://opendict.korean.go.kr/api/view?'

    # key에 우리말샘 오픈 API 이용신청 후 받은 인증키를 넣어줍니다.
    key = 'key=' + opendict_cert_key

    # json 형식으로 반환
    req = "&req_type=json"

    # q에 검색할 문자열을 넣어줍니다.
    q = '&q=' + urllib.parse.quote(query)

    # 정렬 방식(기본값 dict)을 선택합니다. dict: 우리말샘순, popular: 많이 찾은 순, date: 새로 올린 순
    sort = '&sort=dict'

    fullURL = defaultURL + key + req + q + sort

    req = urllib.request.Request(fullURL)
    response = urllib.request.urlopen(req)
    rescode = response.getcode()

    if rescode == 200:
        text = response.read().decode('utf-8')
        jsonObject = json.loads(text)
        jsonItem = jsonObject['channel']['item']

        jsonWord = jsonItem['wordInfo']

        pronunciation = jsonWord['pronunciation_info']
        word_unit = jsonWord['word_unit']
        word = jsonWord['word']
        word_type = jsonWord['word_type']

        jsonSense = jsonItem['senseInfo']

        definition = jsonSense['definition']
        pos = jsonSense['pos']
    else:
        return print('response code:' + rescode)

    print(word)
    print(pronunciation)
    print(word_unit)
    print(word_type)
    print(definition)
    print(pos)


search_for_words_in_opendict("나무001")