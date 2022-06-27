from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from elastic_app_search import Client

client = Client(
    # elastic app search engine의 Credentials
    # https://를 제외한 Endpoint + /api/as/v1
    base_endpoint='my-deployment-a1ad04.ent.us-central1.gcp.cloud.es.io/api/as/v1',
    # elastic app search engine의 private-key
    api_key='private-1x2hnqva8fdxj5msc6eqkhp4',
    use_https=True
)
engine_name = 'dictionary'


def search(request):
    context = []
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        search_result = client.search(engine_name, query, {'sort': {"sense_no": "asc"}})
        for i in range(len(search_result['results'])):
            context.append(search_result['results'][i])
        return render(request, 'dict//searched.html', {'context': context})
    else:
        return render(request, 'dict//searched.html')


def main(request):
    return render(request, 'dict//base.html')


def index(request, pk):
    search_result = client.search(engine_name, pk, {})
    result = search_result['results'][0]
    print(result)
    return render(request, 'dict//item.html', {'result':result})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    return HttpResponse("response" % question_id)


def vote(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)
