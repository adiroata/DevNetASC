from devnet_connection import devnet_connection
from devnet_sandbox import devnet_sandbox
from devnet_loopbacks import loopbacks

# Write a function to establish the remote connection and delete items
def delete_device_config():
    # Open XML template
    config_template = open("XML/delete_config.xml").read()
    for loopback in loopbacks:    
        # Input items into template
        config_delete = config_template.format(INTERFACE=loopback)
        # Edit configuration
        device_reply = devnet_connection.edit_config(target="running", config=config_delete)
        print("\n*** The interface {} was deleted ***".format(loopback))

    devnet_connection.close_session()

# Call function
if __name__=='__main__':
    delete_device_config()