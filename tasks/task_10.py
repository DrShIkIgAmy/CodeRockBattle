import sys
from copy import deepcopy
response = "something: "

def apply_add(base_column, pred):
    col = deepcopy(pred)
    col.sort()
    return [i+j for i,j in zip(base_column,col)]

def decode(inp_str):
    base_column = [x for x in inp_str]
    word_size = 1
    cur_column = base_column
    while word_size < len(inp_str):
        cur_column = apply_add(base_column, cur_column)
        word_size = len(cur_column[0])

    for i in cur_column:
        if i[-1] == '|':
            return i
    return None


for line in sys.stdin:
    line = line.replace('\n','')
    print(decode(line))