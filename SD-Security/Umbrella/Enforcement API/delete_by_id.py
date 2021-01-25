import requests
import os

token = os.environ.get("ENFORCE_API_KEY")
event_id = input("Enter event ID: ")

url = f"https://s-platform.api.opendns.com/1.0/domains/{event_id}?customerKey={token}"

payload={}
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

if response.status_code == 204:
    print("The event was deleted.")
else:
    print("Event not found.")
