from devnet_connection import devnet_connection
from devnet_sandbox import devnet_sandbox

loopbacks = ["Loopback1337", "Loopback1338", "Loopback1339"]

# Write a function to establish the remote connection and set the new config
def edit_device_config():
    # Open XML template
    config_template = open("XML/edit_config.xml").read()
    for loopback in loopbacks:
        # Input items into template
        config_new = config_template.format(INTERFACE=loopback, DESCRIPTION="DevNet test interface")
        device_reply = devnet_connection.edit_config(target="running", config=config_new)
        print("\n*** The interface {} has been configured ***".format(loopback))

# Call function
if __name__=="__main__":
    edit_device_config()