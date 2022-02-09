import sys
response = "something: "
def cycle_shift(inp):
    return [inp[-1]] + [x for x in inp[0:-1]]

def build_shiftlist(inp_word):
    shiftlist = []
    last_shifted = inp_word
    for i in range(len(inp_word)):
        shiftlist.append(cycle_shift(last_shifted))
        last_shifted = shiftlist[-1]
    return shiftlist

for line in sys.stdin:
    line = line.replace('\n','')
    word_list = build_shiftlist(line)
    word_list.sort()
    transformed_str = ''.join([x[-1] for x in word_list])
print(transformed_str)