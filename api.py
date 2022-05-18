import urllib.parse
import urllib.request
import json
import openpyxl

opendict_cert_key = 'FCDE6983D27255C93578050A57CEDFF1'


def search_for_words_in_opendict(words):
    # 마지막이 search면 사전 검색 오픈 API, view면 사전 내용 오픈 API입니다.
    defaultURL = 'https://opendict.korean.go.kr/api/view?'

    # key에 우리말샘 오픈 API 이용신청 후 받은 인증키를 넣어줍니다.
    key = 'key=' + opendict_cert_key

    # json 형식으로 반환
    req = "&req_type=json"
    i = 2
    for query in words:
        # q에 검색할 문자열을 넣어줍니다.
        q = '&q=' + urllib.parse.quote(query)

        # 정렬 방식(기본값 dict)을 선택합니다. dict: 우리말샘순, popular: 많이 찾은 순, date: 새로 올린 순
        sort = '&sort=dict'
        fullURL = defaultURL + key + req + q + sort

        request = urllib.request.Request(fullURL)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if rescode == 200:
            text = response.read().decode('utf-8')
            jsonObject = json.loads(text)
            jsonItem = jsonObject['channel']['item']

            jsonWord = jsonItem['wordInfo']
            ws[columns_a[0] + str(i)] = jsonWord['word']
            ws[columns_a[3] + str(i)] = jsonWord['word_unit']
            ws[columns_a[4] + str(i)] = jsonWord['word_type']
            ws[columns_a[7] + str(i)] = str(jsonWord['pronunciation_info'])

            jsonSense = jsonItem['senseInfo']
            ws[columns_a[2] + str(i)] = jsonSense['definition']

            if 'pos' in jsonSense:
                ws[columns_a[14] + str(i)] = jsonSense['pos']

            ws[columns_a[15] + str(i)] = jsonSense['type']
            ws[columns_a[1] + str(i)] = jsonSense['sense_no']

            if 'original_language_info' in jsonWord:
                jsonOriginal = jsonWord['original_language_info'][0]
                ws[columns_a[5] + str(i)] = jsonOriginal['original_language']
                ws[columns_a[6] + str(i)] = jsonOriginal['language_type']

            if 'conju_info' in jsonWord:
                jsonConju = jsonWord['conju_info'][0]
                if 'conjugation_info' in jsonConju:
                    jsonConjugation = jsonConju['conjugation_info']
                    ws[columns_a[8] + str(i)] = jsonConjugation['conjugation']
                    if 'pronunciation_info' in jsonConjugation:
                        ws[columns_a[9] + str(i)] = str(jsonConjugation['pronunciation_info'])
                if 'abbreviation_info' in jsonConju:
                    jsonAbbre = jsonConju['abbreviation_info']
                    ws[columns_a[10] + str(i)] = jsonAbbre['abbreviation']
                    if 'pronunciation_info' in jsonAbbre:
                        ws[columns_a[11] + str(i)] = str(jsonAbbre['pronunciation_info'])

            if 'origin' in jsonWord:
                ws[columns_a[12] + str(i)] = jsonWord['origin']

            if 'allomorph' in jsonWord:
                ws[columns_a[13] + str(i)] = jsonWord['allomorph']

            if 'cat_info' in jsonSense:
                ws[columns_a[17] + str(i)] = str(jsonSense['cat_info'])

            if 'grammar_info' in jsonSense:
                ws[columns_a[16] + str(i)] = str(jsonSense['grammar'])

            if 'example_info' in jsonSense:
                jsonExam = jsonSense['example_info'][0]
                ws[columns_a[18] + str(i)] = jsonExam['example']
                if 'source' in jsonExam:
                    ws[columns_a[19] + str(i)] = jsonExam['source']
                if 'origin' in jsonExam:
                    ws[columns_a[20] + str(i)] = jsonExam['origin']

            if 'relation_info' in jsonSense:
                relation = ''
                for j in range(len(jsonSense['relation_info'])):
                    relation = relation + jsonSense['relation_info'][j]['word'] + ', '
                ws[columns_a[21] + str(i)] = relation[0:len(relation) - 2]

            if 'translation_info' in jsonSense:
                translation = ''
                for j in range(len(jsonSense['translation_info'])):
                    translation = translation + jsonSense['translation_info'][j]['word'] + ', '
                ws[columns_a[22] + str(i)] = translation[0:len(translation) - 2]
            i += 1
        else:
            return print('response code:' + rescode)


wb = openpyxl.Workbook()

ws = wb.create_sheet('data')

i = 0
columns = ['표제어', '의미번호', '뜻', '구성단위', '고유어 여부', '원어', '언어', '발음', '활용', '활용의 발음', '준말', '준말의 발음', '어원', '이형태', '품사',
           '범주', '문법', '전문분야', '용례', '용례의 출처', '용례의 원문', '관련어', '대역어']
columns_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
for column in columns:
    ws[columns_a[i] + '1'] = column
    i += 1
words = ['ㄱ001', '기린001', '기린002', ]
search_for_words_in_opendict(words)

wb.save(r'D:\신희승\IIRTECH\IIRTECH\data.xlsx')
