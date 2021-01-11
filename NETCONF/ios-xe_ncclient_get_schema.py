from ncclient import manager
import xml.etree.ElementTree as ET

# Connection informations
HOST = "sandbox-iosxe-latest-1.cisco.com"
PORT = "830"
USERNAME = "developer"
PASSWORD = "C1sco12345"

with manager.connect(
    host=HOST, 
    port=PORT, 
    username=USERNAME, 
    password=PASSWORD,
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False
) as CONNECTION:
    SCHEMA = CONNECTION.get_schema("ietf-yang-types")
    ROOT = ET.fromstring(SCHEMA.xml)
    YANG_TREE = list(ROOT)[0].text
    F = open("YANG/ietf-yang-types.yang", "w")
    F.write(YANG_TREE)
    F.close()


# Go to /YANG and run $ pyang -f tree <file name>