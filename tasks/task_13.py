import sys
import re
response = "something: "


def encode_caeser(inp_word):
    lower_case_voc = 'abcdefghijklmnopqrstuvwxyz'
    upper_case_voc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    voc_dim = len(lower_case_voc)
    shift = 0
    dim = len(inp_word)
    if dim == 0:
        return inp_word
    if inp_word[0].isupper():
        shift = upper_case_voc.index(inp_word[0]) + 1
    else:
        shift = lower_case_voc.index(inp_word[0]) + 1
    
    out_put = ''
    for i in range(dim):
        if inp_word[i].isupper():
            cur_pos = upper_case_voc.index(inp_word[i])
            new_pos = (cur_pos + shift) % voc_dim
            out_put += upper_case_voc[new_pos]
        else:
            cur_pos = lower_case_voc.index(inp_word[i])
            new_pos = (cur_pos + shift) % voc_dim
            out_put += lower_case_voc[new_pos]
    return out_put

def encode_replacement(inp_word):
    inp_word.replace('\n','')
    dim = len(inp_word)
    out_put = [None] * dim
    cur_char = 0
    inc = 0
    inc_dir = 1
    trig = False
    while cur_char != dim:
        if trig == False and out_put[inc] == None:
            trig = not trig
        elif trig == True and out_put[inc] == None:
            trig = not trig
            out_put[inc] = inp_word[cur_char]
            cur_char += 1
        if inc + inc_dir == dim or inc + inc_dir < 0:
            inc_dir *= -1
        inc += inc_dir
    
    return ''.join(out_put)

def encode(sentences):
    reg = re.compile(r'[A-Za-z]+')
    words = reg.finditer(sentences)
    for span in words:
        pos = span.span()
        word = sentences[pos[0]:pos[1]]
        new_word = encode_replacement(word)
        new_word = encode_caeser(new_word)
        sentences = sentences[:pos[0]] + new_word + sentences[pos[1]:]
    return sentences

for line in sys.stdin:
    line = line.replace('\n','')
    response = encode(line)
print(response) # print the answer to stdout