curl -k -X POST https://10.10.20.110/nuova \
-H 'Content-Type: application/xml' \
-d '<aaaLogin inName="ucspe" inPassword="ucspe"></aaaLogin>' \
| xmllint --pretty 2 -
echo ''