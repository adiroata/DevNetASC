from ncclient import manager

# # Connection informations
HOST = "sandbox-iosxe-latest-1.cisco.com"
PORT = "830"
USERNAME = "developer"
PASSWORD = "C1sco12345"

# Write a function to establish the remote connection and get device capabilities
def get_capabilities():
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
        print("\n*** Capabilitatile NETCONF pentru echipamentul {} ***".format(HOST))
        for capability in device.server_capabilities:
            print(capability)

# Call function
if __name__=='__main__':
    get_capabilities()

#print("Done!")