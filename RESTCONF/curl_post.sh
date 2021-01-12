CRED_HASH=$(echo -n developer:C1sco12345 | base64)

curl --location --insecure \
--request POST 'https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces' \
--header 'Content-Type: application/yang-data+json' \
--header "Authorization: Basic $CRED_HASH" \
--data-raw '{
    "ietf-interfaces:interface": {
        "name": "Loopback1337",
        "description": "Created in the DevNet Asoc lab",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.168.168.168",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}
'