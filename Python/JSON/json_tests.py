import json

JSON_string = '''{"Key1": true}'''

JSON_dict = json.loads(JSON_string)

# print(type(JSON_dict))
print(JSON_dict["Key1"])

JSON_dict["Key2"] = False

print(JSON_dict)

JSON_string = json.dumps(JSON_dict, indent=2)
print(JSON_string)