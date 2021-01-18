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

# Create headers to be used with GET verb
get_headers = {"Accept": ",".join(accespt_list)}

# Create headers to be used with POST verb
post_headers = {"Content-Type": "application/vnd.yang.data+json"}

# Get a list of all devices
get_resp = requests.get("{}/running/devices/device".format(url_base), auth=basic_auth, headers=get_headers)

# If the list is empty raise error message
if get_resp.status_code != 200:
    raise requests.exceptions.HTTPError("Empty device list")

# Print output
devices = get_resp.json()["collection"]["tailf-ncs:device"]

for device in devices:
    print(json.dumps(device, indent=2, sort_keys=True))