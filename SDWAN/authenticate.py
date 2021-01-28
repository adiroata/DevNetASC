import requests
import json
import os

# Import user & pass from sys vars.
user=os.environ.get("SDWAN_API_USER")
pwd=os.environ.get("SDWAN_API_PASS")

def login(vmanage_ip, j_username, j_password):
    base_url = "https://%s:8443" %(vmanage_ip)
    login_action = "/j_security_check"
    
    # Format data from login form
    login_data = {"j_username": j_username, "j_password": j_password}
    
    # Store cookie in a variable named "session"
    # MUST use a session for SD-WAN
    # Open a new session:
    session = requests.session()
    
    # Login to vManage
    response = session.post(url=f"{base_url}{login_action}", data=login_data, verify=False)
    print(response.status_code)

if __name__=="__main__":
    login("10.10.20.90", user, pwd)