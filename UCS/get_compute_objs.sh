curl -k -X POST https://10.10.20.110/nuova \
-H 'Content-Type: application/xml' \
-d '<configFindDnsByClassId
    classId="computeItem"
    cookie="1612193808/a2517098-53af-45c9-9679-3fb6569c20d3" />'\
| xmllint --pretty 2 -
echo ''