import meraki
import json

# export the meraki API key as environment variable

dashboard = meraki.DashboardAPI()

my_org = dashboard.organizations.getOrganizations()

jsonfile = json.dumps(my_org, indent=2)

print(jsonfile)


# Documentation:
# https://pypi.org/project/meraki/