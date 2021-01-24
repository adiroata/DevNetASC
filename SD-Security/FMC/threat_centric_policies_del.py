import json
import requests
import os
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)

base_url = "https://fmcrestapisandbox.cisco.com"
login_url = "/api/fmc_platform/v1/auth/generatetoken"
headers = {"Content-Type": "application/json"}
user = os.environ.get("FMC_USER")
pw = os.environ.get("FMC_PASS")

login_response = requests.post(f"{base_url}{login_url}", auth=(user, pw), verify=False)

# The token is delivered in the headers (NOT in body of the response)

# Parse the headers 
resp_headers = login_response.headers

# Grab the token
token = resp_headers.get("X-auth-access-token", default=None)

# Append the headers dictionary with the token value
headers["X-auth-access-token"] = token


################################################################

"""
The script searches for a policy by name and gets the policy ID.
After that the DELETE method is called to remove the policy. 
"""


pol_url = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies"

pol_response = requests.get(f"{base_url}{pol_url}", headers=headers, verify=False).json()
# print(json.dumps(pol_response, indent=2, sort_keys=True))

policies_count=int(json.dumps(pol_response["paging"]["count"], indent=2, sort_keys=True))
url_updates = policies_count // 25

policy_name = input("Name of the policy: ")

limit = 25
offset = 0
for lookup in range (url_updates+1):
  policyId = None
  policy_url = f"/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies?offset={offset}&limit={limit}"
  policy_response = requests.get(f"{base_url}{policy_url}", headers=headers, verify=False).json()
  for item in policy_response["items"]:
    if item["name"] == policy_name:
      policyId = item["id"]
      print(f"Found the Policy ID: {policyId}")
      break
    else:
      pass
  if policyId == None:
    offset += 25
  else:
    break


# CLEAN UP 
policy_url_new = f"/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/{policyId}"

print ("******** DELETING POLICY ********")
del_response = requests.delete(f"{base_url}{policy_url_new}", headers = headers, verify = False).json()