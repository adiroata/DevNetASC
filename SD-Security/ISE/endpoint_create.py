import json
import requests

api_user = "ersadmin"
api_pass = "C1sco12345!"

epg_id = input("Enter Endpoint Group ID: ")

base_url = "https://10.10.20.70:9060/ers/config/endpoint"

payload = {
    "ERSEndPoint": {
        "name": "DevNet_Endpoint_2",
        "description": "DevNet Endpoint-2",
        "mac": "FF:EE:DD:03:04:05",
        "groupId": f"{epg_id}",
        "staticGroupAssignment": True
    }
}

headers = {
    "content-type": "application/json",
    "accept": "application/json",
    "cache-control": "no-cache",
}

response = requests.request("POST", base_url, auth=(api_user, api_pass), data=json.dumps(payload), headers=headers, verify=False)

print(response.status_code)