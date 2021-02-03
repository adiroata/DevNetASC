curl -k -X POST \
https://sandboxapicdc.cisco.com/api/aaaLogin.json \
-d '{
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "ciscopsdt"
        }
    }
}' \
| json_reformat

echo ''