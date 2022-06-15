from elastic_app_search import Client
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

search_result = client.search(engine_name, '사람', {})
print(json.dumps(search_result, indent=2, ensure_ascii=False))
