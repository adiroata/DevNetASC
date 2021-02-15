curl -k -X GET \
https://sandboxapicdc.cisco.com/api/node/class/topology/pod-1/topSystem.json \
-H "Cookie: APIC-cookie=$ACI_TOKEN" \
| json_reformat

echo ''