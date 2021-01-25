import requests
import os

token = os.environ.get("ENFORCE_API_KEY")

url = f"https://s-platform.api.opendns.com/1.0/events?customerKey={token}"

payload="""
    {
    "alertTime": "2013-02-08T11:14:26.0Z",
    "deviceId": "ba6a59f4-e692-4724-ba36-c28132c761de",
    "deviceVersion": "13.7a",
    "dstDomain": "internetbadguys4.com",
    "dstUrl": "http://internetbadguys4.com/a-bad-url",
    "eventTime": "2013-02-08T09:30:26.0Z",
    "protocolVersion": "1.0a",
    "providerName": "Security Platform"
    }
"""

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
