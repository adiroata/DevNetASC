# CRED_HASH=$(echo -n developer:C1sco12345 | base64)

curl --location --insecure \
--request GET 'https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces' \
--header 'Accept: application/yang-data+json' \
--header 'Content-Type: application/yang-data+json' \
-u developer:C1sco12345