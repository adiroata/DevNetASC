import json
import requests

api_user = "ersadmin"
api_pass = "C1sco12345!"

base_url = "https://10.10.20.70:9060/ers/config/endpointgroup"

headers = {
    "content-type": "application/json",
    "accept": "application/json",
    "cache-control": "no-cache",
}

response = requests.request("GET", base_url, auth=(api_user, api_pass), headers=headers, verify=False).json()

# print(json.dumps(response, indent=2))

print("{0:50s}{1:1}{2:40s}{3:1}{4:50s}".format("Group Name", "| ", "Group ID", "| ", "Group Description"))
print("="*175)
for item in response["SearchResult"]["resources"]:
    print("{0:50s}{1:1}{2:40s}{3:1}{4:50s}".format(item["name"], "| ", item["id"], "| ", item["description"]))
    print("."*175)