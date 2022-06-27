'''
cloud-id : HeeSeung:YXNpYS1ub3J0aGVhc3QzLmdjcC5lbGFzdGljLWNsb3VkLmNvbSQ4OGFlNzM5MGQ4MmM0YjA0YjMzYjM4NDk0MDBhNTRlNSRlNWZkMTRkZDk5OWE0ZDU2OTU5YjZjNWIyMTgzZDIxMg==
username  elastic
password  BtRlZps4UDAmmBJcOTYnrxz5
'''

from elastic_app_search import Client
import json

client = Client(
    # elastic app search engine의 Credentials
    # https://를 제외한 Endpoint + /api/as/v1
    base_endpoint='my-deployment-a1ad04.ent.us-central1.gcp.cloud.es.io/api/as/v1',
    # elastic app search engine의 private-key
    api_key='private-1x2hnqva8fdxj5msc6eqkhp4',
    use_https=True
)
engine_name = 'dictionary'
document = 'C:\\Users\\82105\\Desktop\\신희승\\IIRTECH\\IIRTECH\\data.json'
with open(document, 'r', encoding='utf-8-sig') as fp:
    json_data = json.load(fp)
count = 0
for i in range(len(json_data)):
    client.index_document(engine_name, json_data[i])
    if i % 100 == 0:
        print(i, 'document art indexed')

'''while count < len(json_data):
    data_end = (count + 100) if (count + 100) < len(json_data) else len(json_data)
    docu = json_data[count:data_end]

    #client.index_document(engine_name, docu)
    print(data_end, 'document art indexed')
    count += 100'''

