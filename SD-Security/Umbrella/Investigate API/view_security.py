import requests
import os
import json

token = os.environ.get("INVESTIGATE_TOKEN")
domain_name = input("Type domain name: ")

url = f"https://investigate.api.umbrella.com/security/name/{domain_name}"

payload={}
headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.request("GET", url, headers=headers, data=payload).json()

print(json.dumps(response, indent=2))