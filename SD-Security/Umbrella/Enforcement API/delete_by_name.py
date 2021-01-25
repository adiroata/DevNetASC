import requests
import os

token = os.environ.get("ENFORCE_API_KEY")
event_name = input("Enter event name: ")

url = f"https://s-platform.api.opendns.com/1.0/domains?customerKey={token}&where[name]={event_name}"

payload={}
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

if response.status_code == 204:
    print("The event was deleted.")
else:
    print("Event not found.")
