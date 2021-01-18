from genie.testbed import load

# Load the testbed
tb = load('testbed.yml')

# Find the device with alias uut
dev = tb.devices['R1']

# Connect to the device
dev.connect()

# Parse the output of the show version command
output = dev.parse('show version')

# Extract the version number and print it to the screen
print('IOS version number: ' + output['version']['version'])