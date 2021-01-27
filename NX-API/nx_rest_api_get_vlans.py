import requests
import json
import os

"""
The script starts by making a POST request in order to refresh the API token.
It follows with a GET request to get all the VLANs configured on the Nexus.
It stores the VLAN IDs into a list, and then prints the sorted list.
"""



name=os.environ.get("NXAPI_USER")
pwd=os.environ.get("NXAPI_PASS")

url = "https://10.10.20.58/api/aaaLogin.json"

payload={ "aaaUser": 
            { "attributes": 
                { "name": f"{name}",
                  "pwd": f"{pwd}"
                }
            }
        }

headers = {
    'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload), verify=False).json()

# print(response["imdata"][0]["aaaLogin"]["attributes"]["token"])

token = response["imdata"][0]["aaaLogin"]["attributes"]["token"]
cookies = {}
cookies["APIC-cookie"]=token

vlans_url = "https://10.10.20.58//api/node/class/l2BD.json"

vlans_response = requests.request("GET", vlans_url, headers=headers, data=payload, cookies=cookies, verify=False).json()

# print(json.dumps(vlans_response, indent=2))

vlans_list=[]

for vlan in vlans_response["imdata"]:
    # print(vlan["l2BD"]["attributes"]["id"])
    vlans_list.append(int(vlan["l2BD"]["attributes"]["id"]))

print(sorted(vlans_list))