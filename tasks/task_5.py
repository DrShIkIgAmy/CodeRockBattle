import sys
import re

reg = r'[А-Я][а-яА-Я]+\s+[А-Я][а-яА-Я]+'
response = "something: "
for line in sys.stdin: # get input strings one by one
    names = re.findall(reg,line)
    for i in names:
        i = ' '.join(i.split(' '))
    response = ', '.join(names)
print(response) # print the answer to stdout