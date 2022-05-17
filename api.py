import urllib.parse
import urllib.request
import json
import openpyxl

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
    i = 2
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

        ws['B' + str(i)] = jsonWord['word']
        ws['C' + str(i)] = jsonWord['word_unit']
        ws['D' + str(i)] = jsonWord['word_type']
        ws['E' + str(i)] = str(jsonWord['pronunciation_info'])
        jsonSense = jsonItem['senseInfo']

        ws['F' + str(i)] = jsonSense['definition']
        ws['G' + str(i)] = jsonSense['pos']
        ws['H' + str(i)] = jsonSense['type']

        if 'cat_info' in jsonSense:
            ws['I' + str(i)] = str(jsonSense['cat_info'])
    else:
        return print('response code:' + rescode)


wb = openpyxl.Workbook()

ws = wb.create_sheet('data')

i = 0
columns = ['index', '표제어', '구성단위', '고유어 여부','원어','언어','발음','활용','활용의 발음','준말','준말의 발음','어원','이형태', '정의', '품사', '범주','문법' , '전문분야']
for column in columns:
    ws[chr(65+i) + '1'] = column
    i += 1
words = ['나무001', '기린001', '기린002', ]
search_for_words_in_opendict("나무001")

wb.save(r'D:\신희승\IIRTECH\IIRTECH\data.xlsx')

''' , 
word : 표제어
word_unit : 구성단위
word_type : 고유어 여부
pronunciation : 발음
definition : 정의
pos : 품사
cat : 전문분야
type = 범주'''