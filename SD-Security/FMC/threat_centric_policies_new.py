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

# Add policy

pol_url = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies"

payload = {
"type": "AccessPolicy",
"name": "DevNet Policy",
"description": "DevNet demo policy",
"defaultAction": {
 "intrusionPolicy": {
   "name": "Security Over Connectivity",
   "id": "abba9b63-bb10-4729-b901-2e2aa0f4491c",
   "type": "IntrusionPolicy"
 },
 "variableSet": {
   "name": "Default Set",
   "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
   "type": "VariableSet"
 },
 "type": "AccessPolicyDefaultAction",
 "logBegin": False,
 "logEnd": True,
 "sendEventsToFMC": True
}
}

policy_response = requests.post(
    f"{base_url}{pol_url}", headers=headers, data=json.dumps(payload), verify=False).json()
print("******** POLICY CREATED ********")
print(json.dumps(policy_response, indent=2, sort_keys=True))
print("******** POLICY CREATED ********")
policyId = policy_response["id"]

policy_url = f"/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/{policyId}"


# Add rules

rules_url = f"{policy_url}/accessrules"

rules_payload = {
  "sendEventsToFMC": True,
  "action": "ALLOW",
  "enabled": True,
  "type": "AccessRule",
  "name": "DevNet DPI Malware Inspect",
  "logFiles": True,
  "logBegin": False,
  "logEnd": False,
  "variableSet": {
    "name": "Default Set",
    "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
    "type": "VariableSet"
  },
  "sourceNetworks": {
    "objects": [{
      "type": "NetworkGroup",
      "name": "IPv4-Private-All-RFC1918",
      "id": "15b12b14-dace-4117-b9d9-a9a7dcfa356f"
    }]
  },
  "filePolicy": {
    "name": "New Malware",
    "id": "59433a1e-f492-11e6-98fd-84ec1dfeed47",
    "type": "FilePolicy"
  }
}

rules_response = requests.post(f"{base_url}{rules_url}", headers = headers, data=json.dumps(rules_payload), verify=False).json()
print("******** RULES CREATED ********")
print(json.dumps(rules_response, indent=2, sort_keys=True))
print("******** RULES CREATED ********")