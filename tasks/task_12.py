import sys
inp_string = ''

def parse_input(input_string):
    input_string = input_string.replace(' ','')
    lines = input_string.split('\n')
    lines = [x for x in lines if x]

    graph = {}
        
    for line in lines:
        decomposed = line.split(':')
        key = decomposed[0]
        vals = list(map(int,decomposed[1].split(',')))
        graph[int(key)] = vals
    
    return graph

def find_pathcount(graph, cur_node = 1, explored_nodes =0, searched_len = 6):
    explored_nodes += 1
    if not (cur_node in graph):
        if explored_nodes >= searched_len:
            return 1
        else:
            return 0
    paths_founded = 0
    for i in graph[cur_node]:
        paths_founded += find_pathcount(graph, cur_node= i, explored_nodes= explored_nodes)
    
    return paths_founded
    
    

for line in sys.stdin:
    inp_string += line
graph = parse_input(inp_string)
path_count = find_pathcount(graph)
print(path_count)