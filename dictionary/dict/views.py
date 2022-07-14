from django.shortcuts import render
from elasticsearch import Elasticsearch
from elastic_app_search import Client
from django.core.paginator import Paginator

'''
원어/ 언어 0
활용/ 발음 0
준말/ 발음 0
용례  0
관련 어휘/ 유형 0
대역어/ 언어 0
속담/뜻풀이/유형 0
'''

es = Elasticsearch(["http://127.0.0.1:9200"])
index = "word"

client = Client(
    # elastic app search engine의 Credentials
    # https://를 제외한 Endpoint + /api/as/v1
    base_endpoint='my-deployment-a1ad04.ent.us-central1.gcp.cloud.es.io/api/as/v1',
    # elastic app search engine의 private-key
    api_key='private-1x2hnqva8fdxj5msc6eqkhp4',
    use_https=True
)
engine_name = 'dictionary'


def get(q):
    if q == "":
        return {}
    query = {
        'match': {
            'word': q
        }
    }
    search_result = es.search(index="word", query=query)
    total = search_result['hits']['total']['value']
    if total == 0:
        return {}
    page = int(total / 10) + 1
    context = []
    for i in range(1, page + 1):
        search_result = es.search(index="word", from_=(i - 1) * 10, query=query)
        for j in range(len(search_result['hits']['hits'])):
            context.append(search_result['hits']['hits'][j]['_source'])
    return context
    # search_result = client.search(engine_name, query, {'sort': {"sense_no": "asc"}})
    # if len(search_result) == 0:
    #     return {}
    # page = search_result['meta']['page']['total_pages']
    # context = []
    # for i in range(1, page + 1):
    #     search_result = client.search(engine_name, query, {
    #         'sort': {"sense_no": "asc"},
    #         'page': {'current': i}
    #     })
    #     for j in range(len(search_result['results'])):
    #         context.append(search_result['results'][j])
    # return context


def search(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        page = request.GET.get('page')  # 페이지
        context = get(query)
        print(context)
        paginator = Paginator(context, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        return render(request, 'dict//searched.html', {'context': page_obj, 'kw': query})
    else:
        return render(request, 'dict//searched.html')


def main(request):
    return render(request, 'dict//base.html')


def get_result(result, string, separator):
    if result[string] is not None:
        return result[string].split(separator)
    return


def get_pro_result(result, string):
    value = []
    if result[string] is not None:
        value = result[string].split('], ')
    for i in range(len(value) - 1):
        value[i] = value[i] + "]"
    return value


def index(request, pk):
    query = {
        'match': {
            'pk': pk
        }
    }
    search_result = es.search(index="word", query=query)
    search_result = search_result['hits']['hits'][0]['_source']
    example = get_result(search_result, "example", ',  ')
    if example is not None:
        last = example[len(example) - 1]
        example[len(example) - 1] = last[0:len(last) - 1]
        for i in range(len(example)):
            example[i] = example[i].replace("}", "").replace("{", "")

    conjugation = get_result(search_result, "conjugation", ', ')
    conjugation_pro = get_pro_result(search_result, "conjugation_pro")
    conju_dic = {}
    if conjugation is not None and conjugation_pro is not None:
        conju_dic = {name: value for name, value in zip(conjugation, conjugation_pro)}

    abbreviation = get_result(search_result, "abbreviation", ', ')
    abbreviation_pro = get_pro_result(search_result, "abbreviation_pro")
    abbre_dic = {}
    if abbreviation is not None and abbreviation_pro is not None:
        abbre_dic = {name: value for name, value in zip(abbreviation, abbreviation_pro)}

    relation_word = get_result(search_result, "relation_word", ', ')
    relation_type = get_result(search_result, "relation_type", ', ')
    relation_dic = {}
    word_list = []
    if relation_word is not None:
        for i in range(len(relation_word)):
            if i != 0 and relation_type[i] != relation_type[i - 1]:
                relation_dic[relation_type[i - 1]] = word_list
                word_list = []
            word_list.append(relation_word[i])
        relation_dic[relation_type[len(relation_type) - 1]] = word_list

    proverb = get_result(search_result, 'proverb', '   ')
    pro_defi = get_result(search_result, 'pro_defi', '   ')
    pro_type = get_result(search_result, 'pro_type', '   ')
    proverb_dict = {}
    if proverb is not None:
        for i in range(len(proverb)):
            proverb_dict[proverb[i]] = {pro_defi[i]: pro_type[i]}

    original_language = get_result(search_result, 'original_language', ', ')
    language_type = get_result(search_result, 'language_type', ', ')
    language_dict = {}
    if original_language is not None:
        language_dict = {name: value for name, value in zip(original_language, language_type)}
    return render(request, 'dict//item.html', {'result': search_result, 'example': example,
                                               'conjugation': conju_dic, 'abbreviation': abbre_dic,
                                               'relation': relation_dic, 'proverb': proverb_dict,
                                               'language': language_dict})
