import sys

def parse_input(inp_string):
    mine_map = []
    steps = []
    lines = inp_string.split('\n')
    lines = [x for x in lines if x!= None]
    for i in lines:
        if i.isupper():
            mine_map.append([x for x in i])
        else:
            steps.append(i)
    return mine_map, steps

def make_move(step):
    step = step.replace(' ','')
    if step == 'right':
        return 0, 1
    if step == 'left':
        return 0, -1
    if step == 'up':
        return -1, 0
    if step == 'down':
        return 1, 0

def is_D_hurt(coord_D, coord_W, bound):
    x_inc = 1 if coord_W[0] < coord_D[0] else -1
    y_inc = 1 if coord_W[1] < coord_D[1] else -1
    cur_coord = [coord_W[0], coord_W[1]]
    while True:
        if cur_coord[0] == coord_D[0] and cur_coord[1] == coord_D[1]:
            return True
        cur_coord = [cur_coord[0] + x_inc, cur_coord[1] + y_inc]
        if cur_coord[0] < 0 or cur_coord[0] >= bound[0] \
                or cur_coord[1] < 0 or cur_coord[1] >= bound[1]:
            return False

def find_characters(mine_map):
    map_size = [len(mine_map), len(mine_map[-1])]
    coord_D = []
    coord_W = []
    for i in range(map_size[0]):
        for j in range(map_size[1]):
            if mine_map[i][j] == 'D':
                coord_D = [i,j]
            if mine_map[i][j] == 'W':
                coord_W = [i,j]
    return coord_D, coord_W

def get_answer(mine_map, steps):
    map_size = [len(mine_map), len(mine_map[-1])]
    coord_D, coord_W = find_characters(mine_map)

    x_d, y_d = make_move(steps[0])
    if coord_D[0]+x_d < 0 or coord_D[1]+y_d < 0 \
            or coord_D[0]+x_d >= map_size[0] or coord_D[1]+y_d >=map_size[1]:
        return 'No'
    mine_map[coord_D[0]][coord_D[1]] = '0'
    coord_D = [coord_D[0]+x_d, coord_D[1]+y_d]
    if mine_map[coord_D[0]][coord_D[1]] == '0':
        return 'No'
    mine_map[coord_D[0]][coord_D[1]] = 'D'

    x_w, y_w = make_move(steps[1])
    coord_W = [coord_W[0]+x_w, coord_W[1]+y_w]
    if coord_W[0] < 0 or coord_W [1] < 0 \
            or coord_W[0] >= map_size[0] or coord_W[1] >=map_size[1]:
        return 'No'
    if mine_map[coord_W[0]][coord_W[1]] == '0':
        return 'No'
    if is_D_hurt(coord_W, coord_D, map_size):
        return 'Yes'
    return 'No'

inp_str = ''
for line in sys.stdin:
    inp_str += line
battle_ground, steps = parse_input(inp_str)
print(get_answer(battle_ground, steps))