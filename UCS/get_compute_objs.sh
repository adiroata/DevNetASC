curl -k -X POST https://10.10.20.110/nuova \
-H 'Content-Type: application/xml' \
-d "<configFindDnsByClassId
    classId='computeItem'
    cookie=$UCS_COOKIE />"\
| xmllint --pretty 2 -
echo ''