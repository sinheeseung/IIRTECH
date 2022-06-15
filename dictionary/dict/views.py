from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from elastic_app_search import Client
from .forms import SearchForm

import json

client = Client(
    # elastic app search engine의 Credentials
    # https://를 제외한 Endpoint + /api/as/v1
    base_endpoint='heeseung-edb12d.ent.ap-northeast-2.aws.elastic-cloud.com/api/as/v1',
    # elastic app search engine의 private-key
    api_key='private-y5d2ucj6oxz85nq1dwvrzbmc',
    use_https=True
)
engine_name = 'korean-dictionary'


def search(request):
        context = [
            {
                "word": "소금",
                "sense_no": "001",
                "definition": "짠맛이 나는 백색의 결정체. 대표적인 조미료로, 주성분은 염화 나트륨이다. 천연으로는 바닷물에 약 2.8% 들어 있으며, 암염으로도 산출된다. 인체의 혈액이나 세포 안에 약 0.71% 들어 있고, 어른의 하루 소요량은 10~20그램이다. 양념, 식품의 저장, 화학 공업의 원료 따위로 쓴다.",
                "word_unit": "어휘",
                "word_type": "고유어",
                "original_language": "null",
                "language_type": "null",
                "pronunciation": "['소금']",
                "conjugation": "null",
                "conjugation_pro": "null",
                "abbreviation": "null",
                "abbreviation_pro": "null",
                "origin": "null",
                "allomorph": "null",
                "pos": "명사",
                "type": "일반어",
                "grammar": "null",
                "cat": "null",
                "example": "{소금} 닷 되.",
                "source": "null",
                "relation_word": "염016, 염화008, 가는-소금001, 돌-소금001, 식염001, 암염001, 왕-소금001, 해염001, 결정-체001, 답승001, 소굼002, 쇠금002, 싹싸기002, 쏘곰001, 쏘굼001, 쏘금001, 탑수이001, 탑쉬001, 솜007, 소곰003, 소곰001",
                "translation": "null",
                "region": "null"
            },
            {
        "word": "소금",
        "sense_no": "002",
        "definition": "물건이 썩는 것을 막고 음식의 맛을 나게 한다는 점에서 사회도덕을 순화ㆍ향상시키는 참신자의 사명을 비유적으로 이르는 말.",
        "word_unit": "어휘",
        "word_type": "고유어",
        "original_language": "null",
        "language_type": "null",
        "pronunciation": "['소금']",
        "conjugation": "null",
        "conjugation_pro": "null",
        "abbreviation": "null",
        "abbreviation_pro": "null",
        "origin": "null",
        "allomorph": "null",
        "pos": "명사",
        "type": "일반어",
        "grammar": "null",
        "cat": "['기독교']",
        "example": "null",
        "source": "null",
        "relation_word": "답승001, 소굼002, 쇠금002, 싹싸기002, 쏘곰001, 쏘굼001, 쏘금001, 탑수이001, 탑쉬001, 솜007, 소곰003, 소곰001",
        "translation": "null",
        "region": "null"
    },
    {
        "word": "소금",
        "sense_no": "003",
        "definition": "우리나라의 타악기의 하나. 면의 지름 28cm, 둘레의 높이 5cm로 징보다 조금 작으며, 붉은 칠을 한 나무망치로 친다.",
        "word_unit": "어휘",
        "word_type": "한자어",
        "original_language": "小金",
        "language_type": "한자",
        "pronunciation": "['소ː금']",
        "conjugation": "null",
        "conjugation_pro": "null",
        "abbreviation": "null",
        "abbreviation_pro": "null",
        "origin": "null",
        "allomorph": "null",
        "pos": "명사",
        "type": "일반어",
        "grammar": "null",
        "cat": "['음악']",
        "example": "null",
        "source": "null",
        "relation_word": "null",
        "translation": "null",
        "region": "null"
    }]
        if 'kw' in request.GET:
            query = request.GET.get('kw')
            print(query)
            return render(request, 'dict//searched.html', {'context':context})
        else:
            return render(request, 'dict//searched.html')

def main(request):
    #search_result = client.search(engine_name, '사람', {})
    return render(request, 'dict//base.html')

def index(request):
    #search_result = client.search(engine_name, '사람', {})
    return HttpResponse("You're looking at question %s")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    return HttpResponse("response" % question_id)


def vote(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)