import requests
import os
import json

token = os.environ.get("ENFORCE_API_KEY")

url = f"https://s-platform.api.opendns.com/1.0/domains?customerKey={token}"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload).json()

# print(json.dumps(response["data"], indent=2, sort_keys=True))

print("{0:15}{1:1}{2:50}".format("ID", " | ", "domain name"))
print("-"*50)
for domain in response["data"]:
    print("{0:15s}{1:1}{2:50s}".format(str(domain["id"]), " | ", domain["name"]))
