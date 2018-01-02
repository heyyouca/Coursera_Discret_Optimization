#Version 1: order and counter order

from collections import namedtuple
from datetime import datetime


def solve_it(input_data):
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    if item_count < 1000:
        Item = namedtuple("Item", ['index', 'value', 'weight','density'])
        for i in range(1, item_count+1):
            line = lines[i]
            parts = line.split()
            items.append(Item(i-1, int(parts[0]), int(parts[1]),int(int(parts[0])/int(parts[1])*10000)))
            sorted_items = sorted(items, key=lambda tup: tup.density, reverse=True)
    
    #function to compute value  based on selected
    #takes in the taken objects and the itmes
    #return value of taken items
    def takenValue(taken):
        value = 0
        for i in range(0,item_count):
            value += taken[i]*items[i].value
        return value
    
    #function to compute weight based on selected
    #takes in the taken objects and the items
    #return weight of taken items
    def takenWeight(taken):
        weight = 0
        for i in range(0,item_count):
            weight += taken[i]*items[i].weight
        return weight
        
    #function to compute best possible value
    #takes in a vector of taken values, depth at measurement and the items
    #return the max value of none already rejected items
    def optimistBound(taken,depth):
        #pick higest relative value and complete to full weight with partial item
        weight = 0
        value = 0
        for i in range(0,depth):
            weight += taken[i]*items[i].weight
            value += taken[i]*items[i].value
        for item in sorted_items:
            if item.index >= depth:
                if weight + item.weight < capacity:
                    value += item.value
                    weight += item.weight
                else:
                    value += item.value*(capacity-weight)/item.weight
                    break
        return value

    #depthFirst search
    def depthFirst(depth,taken,best_taken):
        
        best_value = takenValue(best_taken)
        
        if optimistBound(taken[:],depth) <= best_value:
            return best_taken
        
        if takenWeight(taken) > capacity:
            return best_taken
        
        if depth == item_count:
            return best_taken
        
        if takenValue(taken) > best_value:
            best_taken = taken[:]
        
        taken1 = taken[:]
        taken2 = taken[:]
        taken1[depth] = 1
        depth += 1
        best_taken = depthFirst(depth,taken1,best_taken)
        if depth+1 >= item_count:
            return best_taken
        else:
            taken2[depth] = 1
            best_taken = depthFirst(depth,taken2,best_taken)
        
        return best_taken


    if item_count < 1000:
        taken = [0]*item_count
        depth = 0
        best_taken = [0]*item_count
        start = datetime.now()
        solution = depthFirst(depth,taken,best_taken)
        best = takenValue(solution)
        end = datetime.now()
        print("time:"+str(end - start))
        print("items:"+str(item_count))
      
    # prepare the solution in the specified output format
    output_data = str(best) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))
    
    return output_data

import sys
if len(sys.argv) > 1:
    if __name__ == '__main__':
        if len(sys.argv) > 1:
            file_location = sys.argv[1].strip()+"/data"
            with open(file_location, 'r') as input_data_file:
                input_data = input_data_file.read()
            print(solve_it(input_data))
        else:
            print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
else:
    path = "C:/Users/Heyyou/Dropbox/Private/Code/Discrete Optimization/Week 2/data/"
    file_location = path+"ks_4_0"
    with open(file_location, 'r') as input_data_file:
        input_data = input_data_file.read()
    print(solve_it(input_data))