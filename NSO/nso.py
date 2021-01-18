import requests
import json

url_base = "http://localhost:8080/api"
basic_auth = ("admin", "admin")

accespt_list = [
    "application/vnd.yang.api+json",
    "application/vnd.yang.datastore+json",
    "application/vnd.yang.data+json",
    "application/vnd.yang.collection+json"
]

get_headers = {"Accept": ",".join(accespt_list)}

post_headers = {"Content-Type": "application/vnd.yang.data+json"}

get_resp = requests.get("{}/running/devices/device".format(url_base), auth=basic_auth, headers=get_headers)

if get_resp.status_code != 200:
    raise requests.exceptions.HTTPError("Empty device list")

devices = get_resp.json()["collection"]["tailf-ncs:device"]

for device in devices:
    output = json.dumps(device, indent=2)
    print(output)