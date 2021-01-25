import requests
import os
import json

token = os.environ.get("INVESTIGATE_TOKEN")
domain_name = input("Type domain name: ")

url = f"https://investigate.api.umbrella.com/domains/categorization/{domain_name}?showlabels"

payload={}
headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.request("GET", url, headers=headers, data=payload).json()

# print(json.dumps(response, indent=2))

print("-"*50)
if response[f"{domain_name}"]["status"] == -1:
    print("Site is malicious.")
elif response[f"{domain_name}"]["status"] == 0:
    print("Site is not categorized")
elif response[f"{domain_name}"]["status"] == 1:
    print("Site is ok.")

print("-"*50)
if response[f"{domain_name}"]["security_categories"] == []:
    print("Security threats list is empty.")
else:
    print("Potential risks: ")
    for item in response[f"{domain_name}"]["security_categories"]:
        print("- " + item)

print("-"*50)
if response[f"{domain_name}"]["content_categories"] == []:
    print("List is empty.")
else:
    print("Contents list: ")
    for item in response[f"{domain_name}"]["content_categories"]:
        print("- " + item)