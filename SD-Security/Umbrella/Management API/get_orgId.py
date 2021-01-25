import base64
import requests
import os

url = "https://management.api.umbrella.com/v1/organizations"
headers = {
    "accept": "application/json"
}
api_key = os.environ.get("UMBRELLA_API_KEY")
api_secret = os.environ.get("UMBRELLA_API_SECRET")

# print(user, pw)

response = requests.get(f"{url}", auth=(api_key, api_secret), headers = headers)

print(response.text)
