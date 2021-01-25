import requests
import os
import json

url = "https://management.api.umbrella.com/v1/organizations"
headers = {
    "accept": "application/json"
}
api_key = os.environ.get("UMBRELLA_API_KEY")
api_secret = os.environ.get("UMBRELLA_API_SECRET")

response = requests.get(f"{url}", auth=(api_key, api_secret), headers = headers).json()

orgId=response[0]["organizationId"]

url_policy = f"{url}/{orgId}/policies"

querystring = {"page":"1","limit":"100","type":"dns"}

response_policy = requests.get(f"{url_policy}", auth=(api_key, api_secret), headers = headers, params=querystring).json()

print(json.dumps(response_policy, indent=2, sort_keys=True))