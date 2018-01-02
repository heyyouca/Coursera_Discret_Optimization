#Version 2: some optimization

from collections import namedtuple
from datetime import datetime
from math import ceil


def solve_it(input_data):
    # parse the input
    def rescale(x,scale):
        return int(ceil(x / scale))
    
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    scale = 1
    if capacity*item_count > 100000000:
        scale = 1

    capacity = rescale(capacity,scale)
    
    items = []

    Item = namedtuple("Item", ['index', 'value', 'weight'])
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), rescale(int(parts[1]),scale)))
        items = sorted(items, key=lambda tup: tup.value, reverse=False)
    
    #function to compute value  based on selected
    #takes in the taken objects and the itmes
    #return value of taken items
    def takenValue(taken,items):
        items = sorted(items, key=lambda tup: tup.index, reverse=False)
        value = 0
        for i in range(0,item_count):
            value += taken[i]*items[i].value
        return value
    
    
    #dynamic programming search
    def fillingCol():
        lowest_weight = items[0].weight
        table_value= []
        col_value = [0]*(capacity+1)
        table_value.append(col_value[:])
        for i in range(item_count):
            item = items[i]
            col_value = [0]*(capacity+1)
            value = item.value
            weight = item.weight
            for w in range(lowest_weight,capacity+1):
                if weight > w:
                    col_value[w] = table_value[i][w]
                elif value + table_value[i][w-weight] > table_value[i][w]:
                    col_value[w] = value + table_value[i][w-weight]
                else:
                    col_value[w] = max(value, table_value[i][w])
            table_value.append(col_value[:])
        return table_value
    
    def rollBack(table_value):
        col = item_count
        row = capacity
        used = []
        for i in range(item_count):
            if table_value[col][row] > table_value[col-1][row]:
                used.append(items[col-1].index)
                row -= items[col-1].weight
            col -= 1
        return used
    
    start = datetime.now()
    table_value = fillingCol()
    used = rollBack(table_value)
    end = datetime.now()
    print("time:"+str(end - start))
    print("items:"+str(item_count))
    solution = [0]*item_count
    for index in used:
        solution[index] = 1
    
    perfect = 0
    if scale == 1:
        perfect = 1
    # prepare the solution in the specified output format
    output_data = str(takenValue(solution,items[:])) + ' ' + str(perfect) + '\n'
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
    file_location = path+"ks_200_1"
    with open(file_location, 'r') as input_data_file:
        input_data = input_data_file.read()
    print(solve_it(input_data))