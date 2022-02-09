import sys
response = ''

def build_voc():
    alphabet_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphabet_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    voc = {}
    for i in range(16):
        voc[alphabet_lower[i]] = alphabet_lower[15 - i]
        voc[alphabet_upper[i]] = alphabet_upper[15 - i]

        voc[alphabet_lower[16+i]] = alphabet_lower[16+15 - i]
        voc[alphabet_upper[16+i]] = alphabet_upper[16+15 - i]
    return voc

for line in sys.stdin: # get input strings one by one
    voc = build_voc()
    for i in line:
        if i.isalpha():
            response += voc[i]
        else:
            response += i
print(response) # print the answer to stdout