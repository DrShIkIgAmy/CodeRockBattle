import sys
response = "something: "
inp_lines = ''

SIZE = 5

matrix_LU = []
matrix_RU = []
matrix_LD = []
matrix_RD = []
word_to_encode = ''

def fill_matrix(mtx, rows):
    for i in rows:
        mtx.append([el for el in i.split(',')])

def parse_input(inp):
    lines = inp.split('\n')
    lines = [x for x in lines if x]
    fill_matrix(matrix_LU, lines[0:5])
    fill_matrix(matrix_RU, lines[5:10])
    fill_matrix(matrix_LD, lines[10:15])
    fill_matrix(matrix_RD, lines[15:20])
    return lines[20]

def find_alpha_in_mtx(mtx, alpha):
    if alpha == 'I' or alpha == 'J':
        alpha = 'I/J'
    for i in range(SIZE):
        for j in range(SIZE):
            if mtx[i][j] == alpha:
                return i, j

def prepare_sentence(encode_str):
    prepared_pairs = []
    last_char = None
    raw_encode = encode_str.replace(' ','')
    if len(raw_encode) % 2 != 0:
        last_char = raw_encode[-1]
    for i in range(len(raw_encode)//2):
        prepared_pairs.append([raw_encode[i*2], raw_encode[i*2+1]])
    return prepared_pairs, last_char

def encode_pair(pair, matrices):
    fx, fy = find_alpha_in_mtx(matrices[0], pair[0])
    sx, sy = find_alpha_in_mtx(matrices[3], pair[1])
    return ''.join([matrices[1][fx][sy],matrices[2][sx][fy]])

def encode_string(inp_str, matrices):
    res_str = ''
    pairs, reminder = prepare_sentence(inp_str)
    for i in pairs:
        res_str += encode_pair(i,matrices)
    if reminder != None:
        res_str += reminder
    return res_str



for line in sys.stdin: # get input strings one by one
    inp_lines += line


word_to_encode = parse_input(inp_lines)
encoded = encode_string(word_to_encode, [matrix_LU, matrix_RU, matrix_LD, matrix_RD])
print(encoded)