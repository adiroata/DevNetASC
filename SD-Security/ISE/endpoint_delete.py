import json
import requests

api_user = "ersadmin"
api_pass = "C1sco12345!"

endpoint_id = input("Enter Endpoint ID: ")

base_url = f"https://10.10.20.70:9060/ers/config/endpoint/{endpoint_id}"

headers = {
    "content-type": "application/json",
    "accept": "application/json",
    "cache-control": "no-cache",
}

response = requests.request("DELETE", base_url, auth=(api_user, api_pass), headers=headers, verify=False)

print(response.status_code)