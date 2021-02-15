curl -k -X GET \
https://sandboxapicdc.cisco.com/api/node/class/fabricPod.json \
-H "Cookie: APIC-cookie=$ACI_TOKEN" \
| json_reformat

echo ''