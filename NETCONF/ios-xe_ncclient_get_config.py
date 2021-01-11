from devnet_connection import devnet_connection
import xml.dom.minidom as xmlparser
from devnet_loopbacks import loopbacks

# Function to view specified items
def view_device_config():
    # Open XML template
    config_template = open("XML/filter_config.xml").read()
    for loopback in loopbacks:
        # Input items into template
        config_filter = config_template.format(INTERFACE=loopback)
        # View item
        item_config = devnet_connection.get(config_filter)
        xmlDom = xmlparser.parseString(str(item_config))
        print("+"*25 + " " + loopback + " " + "+"*25 )
        print(xmlDom.toprettyxml(indent="    "))

    devnet_connection.close_session()

# Call function
if __name__=="__main__":
    view_device_config()