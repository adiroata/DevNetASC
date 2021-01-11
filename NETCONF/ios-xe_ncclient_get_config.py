from ncclient import manager
import xml.etree.ElementTree as ET

# Connection informations
HOST = "ios-xe-mgmt.cisco.com"
PORT = "10000"
USERNAME = "developer"
PASSWORD = "C1sco12345"

netconf_filter = """
 <filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback1337</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback1337</name>
    </interface>
  </interfaces-state>
</filter>
"""

with manager.connect(
    host=HOST, 
    port=PORT, 
    username=USERNAME, 
    password=PASSWORD,
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False
) as CONNECTION:
    print(CONNECTION.get_config("running"))
    # RUNNING_CONF = CONNECTION.get_config("running", netconf_filter)
    # TREE = ET.fromstring(RUNNING_CONF)
    # # ROOT = TREE.getroot()
    # print(TREE)

    # ROOT = ET.fromstring(RUNNING_CONF.xml)
    # RC_TEXT = str(ROOT.text)
    # F = open("FILES/{}.cfg".format(HOST), "w")
    # F.write(RC_TEXT)
    # F.close()

    # print(RC_TEXT)