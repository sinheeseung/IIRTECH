from elasticsearch import Elasticsearch, helpers
import json


def make_index(es, index_name):
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
    print(es.indices.create(index=index_name))


document = 'C:\\Users\\82105\\Desktop\\신희승\\IIRTECH\\IIRTECH\\data.json'
es = Elasticsearch(["http://127.0.0.1:9200"])

index_name = "word"
make_index(es, index_name)
with open(document, 'r', encoding='utf-8-sig') as fp:
    json_data = json.load(fp)
i = 0
data = [
    {
        "_index": index_name,
        "_source": json_data[i]
    }
    for i in range(len(json_data))
]

helpers.bulk(es, data)
# print(es.search(index=index_name, query={'match':{'_source': {}}}))
# '''
# cloud-id : HeeSeung:YXNpYS1ub3J0aGVhc3QzLmdjcC5lbGFzdGljLWNsb3VkLmNvbSQ4OGFlNzM5MGQ4MmM0YjA0YjMzYjM4NDk0MDBhNTRlNSRlNWZkMTRkZDk5OWE0ZDU2OTU5YjZjNWIyMTgzZDIxMg==
# username  elastic
# password  BtRlZps4UDAmmBJcOTYnrxz5
# '''
#
# from elastic_app_search import Client
# import json
#
# client = Client(
#     # elastic app search engine의 Credentials
#     # https://를 제외한 Endpoint + /api/as/v1
#     base_endpoint='my-deployment-a1ad04.ent.us-central1.gcp.cloud.es.io/api/as/v1',
#     # elastic app search engine의 private-key
#     api_key='private-1x2hnqva8fdxj5msc6eqkhp4',
#     use_https=True
# )
# engine_name = 'dictionary'
# document = 'C:\\Users\\82105\\Desktop\\신희승\\IIRTECH\\IIRTECH\\data.json'
# with open(document, 'r', encoding='utf-8-sig') as fp:
#     json_data = json.load(fp)
# count = 0
# for i in range(len(json_data)):
#     client.index_document(engine_name, json_data[i])
#     if i % 100 == 0:
#         print(i, 'document are indexed')
