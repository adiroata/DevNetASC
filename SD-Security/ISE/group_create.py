import json
import requests

api_user = "ersadmin"
api_pass = "C1sco12345!"

base_url = "https://10.10.20.70:9060/ers/config/endpointgroup"

payload = {
    "EndPointGroup": {
        "name": "DevNetGroup",
        "description": "DevNet Associate Group"
    }
}

headers = {
    "content-type": "application/json",
    "accept": "application/json",
    "cache-control": "no-cache",
}

response = requests.request("POST", base_url, auth=(api_user, api_pass), data=json.dumps(payload), headers=headers, verify=False)

print(response.status_code)