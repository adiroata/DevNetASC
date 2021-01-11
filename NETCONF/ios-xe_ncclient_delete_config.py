from ncclient import manager

# # Connection informations
HOST = "ios-xe-mgmt.cisco.com"
PORT = "10000"
USERNAME = "developer"
PASSWORD = "C1sco12345"

new_config="""
<config>
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface operation="delete">
<name>Loopback1337</name>
<description>DevNet Test</description>
<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
<enabled>false</enabled>
</interface>
</interfaces>
</config>
"""

# Write a function to establish the remote connection and get device capabilities
def edit_config():
    # Generate the connection
    with manager.connect(
        host=HOST,
        port=PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False,
        # I set the below args to 'False' to avoid "SSHException('No existing session')" error.
        allow_agent=False,
        look_for_keys=False
    ) as device:

    # Get device capabilities
        print("\n*** The host {} is being configurated ***".format(HOST))
        device_reply = device.edit_config(target="running", config=new_config)

# Call function
if __name__=='__main__':
    edit_config()

#print("Done!")