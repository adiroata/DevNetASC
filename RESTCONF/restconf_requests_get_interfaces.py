import requests
import json

#url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

payload={}
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()

print(json.dumps(response, indent=2))
