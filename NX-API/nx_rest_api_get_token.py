import requests
import json
import os

"""
The script starts by making a POST request in order to refresh the API token.
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

print("The API token is: " + response["imdata"][0]["aaaLogin"]["attributes"]["token"])