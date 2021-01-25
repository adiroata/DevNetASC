import requests
import os
import json

token = os.environ.get("INVESTIGATE_TOKEN")
domain = input("Type domain name: ")

url = f"https://investigate.api.umbrella.com/whois/{domain}.json"

payload={}
headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.request("GET", url, headers=headers, data=payload).json()

print(json.dumps(response, indent=2))
