import re
import json

data = '''
1     enable  down           auto          off/off       enable       Block
2     enable  down           auto          off/off       enable       Block
3     enable  down           auto          off/off       enable       Block
4     enable  down           auto          off/off       enable       Block
5     enable  down           auto          off/off       enable       Block
7     enable  down           auto          off/off       enable       Block
8     enable  down           auto          off/off       enable       Block
9     enable  down           auto          off/off       enable       Block
11    enable  down           auto          off/off       enable       Block
12    enable  down           auto          off/off       enable       Block
13    enable  down           auto          off/off       enable       Block
14    enable  down           auto          off/off       enable       Block
15    enable  down           auto          off/off       enable       Block
16    enable  down           auto          off/off       enable       Block
17    enable  down           auto          off/off       enable       Block
18    enable  down           auto          off/off       enable       Block
19    enable  down           auto          off/off       enable       Block
20    enable  down           auto          off/off       enable       Block
21    enable  down           auto          off/off       enable       Block
22    enable  down           auto          off/off       enable       Block
23    enable  down           auto          off/off       enable       Block
24    enable  down           auto          off/off       enable       Block
27    enable  down           auto          off/off       enable       Block'''

lines = re.split(" ", data)
 
output=[] 
for line in lines:
    if line != '':
        output.append(line)

new_list = [i.split("\n", 1) for i in output]

new_output=[]
output_dict={}

x = (len(new_list)-1)

for n in range(0, x, 6):
    output_dict["port_id"]=new_list[n][1]
    output_dict["admin_stat"]=new_list[n+1]
    output_dict["oper_stat"]=new_list[n+2]
    output_dict["duplex"]=new_list[n+3]
    output_dict["flow"]=new_list[n+4]
    output_dict["mac_learn"]=new_list[n+5]
    output_dict["status"]=new_list[n+6][0]

    new_output.append(output_dict.copy())

print(json.dumps(new_output, indent=2))