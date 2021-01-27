import requests
import json
import os

"""
The script starts by making a POST request in order to refresh the API token.
It follows with a GET request to get all the VLANs configured on the Nexus.
It stores the VLAN IDs into a list, and then prints the sorted list.

It then reads the sorted list and makes a new VLAN with the first available ID.
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

vlans_list = sorted(vlans_list)

n = 1
for vlan in vlans_list:
    print(vlan)
    print(n)
    if n != vlan:
        new_vlan_url = f"https://10.10.20.58/api/node/mo/sys/bd/bd-[vlan-{n}].json"
        new_payload={
            "l2BD": 
            {
                "attributes": 
                {
                    "dn":f"sys/bd/bd-[vlan-{n}]",
                    "fabEncap": f"vlan-{n}",
                    "hwId": f"{n}",
                    "id": f"{n}"
                }
            }
        }
        new_headers = {
            'Content-Type': 'application/json'}
        new_vlan_response = requests.request("PUT", new_vlan_url, 
            headers=new_headers, 
            cookies=cookies, 
            data=json.dumps(new_payload), 
            verify=False).json()
        break
    n +=1

print("+++++   Added new VLAN: "+str(n)+"     +++++")