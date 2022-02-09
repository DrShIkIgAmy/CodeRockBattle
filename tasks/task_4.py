import sys
response = ""

def applyRLE(inp_str):
    res_str = ''
    cur_part = []
    for i in inp_str:
        if cur_part.count(i) == 0 and len(cur_part) > 0:
            res_str += f'{len(cur_part)}{cur_part[0]},'
            cur_part = []
            cur_part.append(i)
        else:
            cur_part.append(i)
    res_str += f'{len(cur_part)}{cur_part[0]}'
    return res_str

for line in sys.stdin: # get input strings one by one
    line = line.replace('\n','')
    response = applyRLE(line)
print(response) # print the answer to stdout