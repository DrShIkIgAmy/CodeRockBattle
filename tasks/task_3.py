import sys
response = ""

def key_builder(lock):
    key_len = lock[-1]
    key_shape = ['0'] * key_len
    key_base = ['X'] * key_len
    for i in range(0, len(lock)-1):
        insert_idx = lock[i]-1
        if insert_idx < 0:
            continue
        key_shape[insert_idx] = 'X'
    if key_len > (lock[-2] + 1):
        key_shape[key_len - 1] = 'X'
    return key_shape, key_base

for line in sys.stdin: # get input strings one by one
    key_height = 3
    lock_map = list(map(int, line.split(',')))
    key_shape, key_base = key_builder(lock_map)
    key_shape = ''.join(key_shape)
    key_base = ''.join(key_base)
    for i in range(key_height):
        response+=key_shape+'\n'
    response += key_base
    
print(response) # print the answer to stdout