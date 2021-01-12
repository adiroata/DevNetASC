CRED_HASH=$(echo -n developer:C1sco12345 | base64)

#echo $CRED_HASH

curl --location --insecure \
--request GET "https://ios-xe-mgmt.cisco.com:9443/restconf/data/netconf-state/capabilities" \
--header "Authorization: Basic $CRED_HASH"