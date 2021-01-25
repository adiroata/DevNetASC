import requests
import os
import json

token = os.environ.get("INVESTIGATE_TOKEN")
domain_name = input("Type domain name: ")

url = f"https://investigate.api.umbrella.com/domains/categorization/{domain_name}?showlabels"

payload={}
headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.request("GET", url, headers=headers, data=payload).json()

# print(json.dumps(response, indent=2))

if response[f"{domain_name}"]["security_categories"] == []:
    print("Domain name looks ok.")
else:
    print("Potential risks: ")
    for item in response[f"{domain_name}"]["security_categories"]:
        print(item)