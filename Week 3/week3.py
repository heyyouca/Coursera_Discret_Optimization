# Week 3 Notes and Commands
cd C:\04 Elearning\CS\Discrete Optimization\Week 3

# Test the command with data
python ./solver.py ./data/gc_20_1

# change wd
import os
os.chdir(r'C:\04 Elearning\CS\Discrete Optimization\Week 3')


# to put a input in memory
file_location = './data/gc_4_1'
with open(file_location, 'r') as input_data_file:
    input_data = input_data_file.read()


# Submit command
python ./submit.py
