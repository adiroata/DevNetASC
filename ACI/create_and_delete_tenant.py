from acitoolkit.acitoolkit import *

user = "admin"
pwd = "ciscopsdt"
url = "https://sandboxapicdc.cisco.com"

session = Session(url, user, pwd)

session.login()

tenants = Tenant.get(session)

# List all the tenants
# for tenant in tenants:
#     print(tenant.name)
#     print(tenant.descr)
#     print("-"*30)

# Create a new Tenant
# new_tenant = Tenant("DevNet_Adrian_Org")

# Create the application profile and the EPG
# anp = AppProfile("Adrian_app", new_tenant)
# epg = EPG("Adrian_epg", anp)

# # Create L3 namespace
# context = Context("Adrian_VRF", new_tenant)
# bridge_domain = BridgeDomain("Adrian_bd", new_tenant)

# # Associate the BD with L3 namespace
# bridge_domain.add_context(context)
# epg.add_bd(bridge_domain)

# # Tenant Creation is completed
# print(new_tenant.get_url())
# print(new_tenant.get_json())
# response = session.push_to_apic(
#     new_tenant.get_url(), data=new_tenant.get_json())
# print(response)

tenants = Tenant.get(session)
for tenant in tenants:
    if tenant.name == "DevNet_Adrian_Org":
        print (tenant.name)
    else:
        print("not found")
        # print(tenant.name)
        # print(tenant.descr)
        # print("-"*30)


# Delete tenant
# new_tenant.mark_as_deleted()
# session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
