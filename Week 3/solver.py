import helpers as hp
import imp
from datetime import datetime
from copy import deepcopy

imp.reload(hp)

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')


    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    #list number of edges coming out of each node
    edge_count = [0] * node_count
    for edge in edges:
        edge_count[edge[0]] += 1
        edge_count[edge[1]] += 1

    
    ### Constraints store, feasability/propagation
    ## Max numer of colors
    # Feasability: this will limit availble colors so that when a set is nodes' color set is empty, know path is not feasible
    # def is_any_node_empty(nodes): # nodes: a LIST of nodes

    ## Two connected nodes cannot have same color
    # Feasability: check is a node can have desired color
    # propagation: when a node's color set has only 1 element left, connect nodes cannot have that color
    # def prop_not_same_color(all_nodes, edges=edges): # this create a tons of re-work over time...
    # def update_solution(solution, all_nodes):

    # There is some symmetry, as of now:
        # First color always 0

#        print("!!!NEW CALL!!!")
#        print("to_color: "+str(to_color))
#        print("color: "+str(color))
#        print("solution: "+str(solution))
#        print("todo_nodes: "+str(todo_nodes))
#        print("all_nodes start: "+str(all_nodes))

    def branch_and_prune(to_color, color, solution, todo_nodes, all_nodes, edges=edges):
        
        # Color
        print("To do: "+str(len(todo_nodes)))
        solution[to_color] = color
        todo_nodes.remove(to_color)
        all_nodes[to_color] = [color]

        # Stopping conditions
        if not(-1 in solution):
            return solution
        elif hp.is_any_node_empty(all_nodes):
            return None
        
        # Propagate
        done = False
        while not(done):
            all_nodes_temp = deepcopy(all_nodes)
            all_nodes = hp.prop_not_same_color(all_nodes, edges)
            if hp.is_any_node_empty(all_nodes):
                return None
            if all_nodes_temp == all_nodes:
                done = True
                
        solution = hp.update_solution(solution,all_nodes)
        if not(-1 in solution):
            return solution
                
        # Pick next node to color and which color: node with less options, then most edges
        candidates = hp.with_less_color_left(all_nodes)
        to_color = hp.node_with_most_edges(candidates,edge_count)
        
        for i in all_nodes[to_color]:
            solution_copy = deepcopy(solution)
            all_nodes_copy = deepcopy(all_nodes)
            solution = branch_and_prune(to_color, i, solution[:], todo_nodes.copy(), deepcopy(all_nodes), edges=edges)
            if not(solution == None):
                return solution
            solution = solution_copy
            all_nodes = all_nodes_copy
        return None

    
    ### Search space
    # Defining list of nodes, each node being a set of available colors
    maxs = {50: 6, 70: 19, 100: 17, 250: 92, 500: 18, 1000: 110}
    max_nb_color = maxs[node_count]
    all_nodes = []
    for i in range(0, node_count):
        all_nodes.append(list(range(0,max_nb_color)))
    solution = [-1] * node_count
    todo_nodes = set(range(0, node_count))
    init_to_color = hp.node_with_most_edges(todo_nodes,edge_count)
    init_color = 0
    start = datetime.now()
    solution = branch_and_prune(init_to_color, init_color, solution, todo_nodes, all_nodes, edges=edges)
    end = datetime.now()
    print("time:"+str(end - start))
    
#    for i in range(2,100):
#        start = datetime.now()
#        print(i)
#        max_nb_color = i
#        all_nodes = []
#        for i in range(0, node_count):
#            all_nodes.append(list(range(0,max_nb_color)))
#        solution = [-1] * node_count
#        todo_nodes = set(range(0, node_count))
#        init_to_color = hp.node_with_most_edges(todo_nodes,edge_count)
#        init_color = 0
#        solution = branch_and_prune(init_to_color, init_color, solution, todo_nodes, all_nodes, edges=edges)
#        end = datetime.now()
#        print("time:"+str(end - start))
#        if not(solution == None):
#            break

    # prepare the solution in the specified output format
    output_data = str(max(solution)+1) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        file_location = './data/gc_70_7'
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))

