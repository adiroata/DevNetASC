import requests
import json
import os


switchuser=os.environ.get("NXAPI_USER")
switchpassword=os.environ.get("NXAPI_PASS")


url='http://10.10.20.58/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show interface description",
    "output_format": "json"
  }
}

url='https://10.10.20.58/ins'
response = requests.post(url,data=json.dumps(payload), 
  headers=myheaders, 
  auth=(switchuser,switchpassword), 
  verify=False).json()

print(json.dumps(response, indent=2))