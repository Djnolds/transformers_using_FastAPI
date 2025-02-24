import requests
import json
url = 'http://127.0.0.1:8000/orders_pydantic'
headers = {
    'accept': 'application/json'
}
params = {
    'product': '',
    'units': ''
}

response = requests.post(url, headers=headers, data=json.dumps(params))

print(response.json())