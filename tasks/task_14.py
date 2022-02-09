import sys
inp_data = ''

def bellman_alg(val_mat, cur_step, days_left):
    vect = val_mat[cur_step][0:days_left + 1]
    if cur_step == 0:
        return max(vect)
    step_res = [
        vect[i] + bellman_alg(val_mat, cur_step - 1, days_left - i)
        for i in range(len(vect))
    ]
    return max(step_res)

def parse_inp(inp_string):
    lines = inp_string.split('\n')
    lines = [line for line in lines if line]
    inv_count = int(lines[0])
    day_count = int(lines[1])
    val_mat = []
    for line in lines[2:]:
        #line = '0,'+line
        val_mat.append(
            [int(x) for x in line.split(',')]
        )
    return val_mat, inv_count, day_count

for line in sys.stdin:
    inp_data+=line
val_mat, inv_count, day_count = parse_inp(inp_data)
print(bellman_alg(val_mat, inv_count-1, day_count))