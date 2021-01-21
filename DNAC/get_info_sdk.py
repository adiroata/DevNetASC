from dnacentersdk import api

# Create a DNACenterAPI connection object;
# it uses DNA Center sandbox URL, username and password

DNAC = api.DNACenterAPI(base_url="https://sandboxdnac2.cisco.com", username="devnetuser", password="Cisco123!")

# Find all devices

DEVICES = DNAC.devices.get_device_list()

# Print select information about the retrieved devices
print("-"*95)
print("{0:25s}{1:1}{2:45s}{3:1}{4:15s}".format("Device Name", "| ", "Device Type", "| ", "Uptime"))
print("-"*95)

try:
    for DEVICE in DEVICES.response:
        print("{0:25s}{1:1}{2:45s}{3:1}{4:15s}".format(DEVICE.hostname, "| ", DEVICE.type, "| ", DEVICE.upTime))
    print("-"*95)
except:
    print()

#print("-"*95)

# Get the health of all clients on Thursday, January 21, 2021 6:00:00 PM [epoch time in miliseconds]
# Epoch time converter: https://www.epochconverter.com/
CLIENTS = DNAC.clients.get_overall_client_health(timestamp=1611252000000)

# Print select information about the retrieved client health statistics
print("{0:25s}{1:1}{2:45s}{3:1}{4:15s}".format("Client Category", "| ", "Number of Clients", "| ", "Client score"))
print("-"*95)

for CLIENT in CLIENTS.response:
    for score in CLIENT.scoreDetail:
        print("{0:25s}{1:1}{2:<45d}{3:1}{4:<15d}".format(score.scoreCategory.value, "| ", score.clientCount, "| ", score.scoreValue))

print("-"*95)