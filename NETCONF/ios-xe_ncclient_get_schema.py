from devnet_connection import devnet_connection
import xml.etree.ElementTree as ET

# # Schema name
YANG_MODEL = "ietf-interfaces"

# Generate a function to collect schema
def get_schema():
    # Generate the connection and get the schema
    SCHEMA = devnet_connection.get_schema(YANG_MODEL)
    ROOT = ET.fromstring(SCHEMA.xml)
    YANG_TREE = list(ROOT)[0].text
    F = open("YANG/{}.yang".format(YANG_MODEL), "w")
    F.write(YANG_TREE)
    F.close()

if __name__=="__main__":
    get_schema()

# Go to /YANG and run $ pyang -f tree <file name>