'''
cloud-id : HeeSeung:YXNpYS1ub3J0aGVhc3QzLmdjcC5lbGFzdGljLWNsb3VkLmNvbSQ4OGFlNzM5MGQ4MmM0YjA0YjMzYjM4NDk0MDBhNTRlNSRlNWZkMTRkZDk5OWE0ZDU2OTU5YjZjNWIyMTgzZDIxMg==
username  elastic
password  Xwg2HcUFRjr1q4X7Sc7M4vkQ

'''
from elastic_app_search import Client
import json

client = Client(
    # elastic app search engine의 Credentials
    # https://를 제외한 Endpoint + /api/as/v1
    base_endpoint='heeseung.ent.asia-northeast3.gcp.elastic-cloud.com/api/as/v1',
    # elastic app search engine의 private-key
    api_key='private-k74157hj169vkcfywae4u6db',
    use_https=True
)
engine_name = 'korean-dictionary'
document = {
    'name' : 'asdf',
    'verv' : 'heeseung',
    'a' : 'ㅁㄴㅇㄹ'
}
client.index_document(engine_name, document)