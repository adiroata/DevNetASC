from devnet_connection import devnet_connection
import xml.etree.ElementTree as ET

# Set a XML filter to extract config
config_template = open("XML/filter_config.xml").read()
config_filter = config_template.format(INTERFACE="Loopback1337", DESCRIPTION="DevNet test interface")

def view_device_config():
    print(devnet_connection.get_config("running", config_filter))

# Call function
if __name__=="__main__":
    view_device_config()