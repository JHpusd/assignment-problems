import sys
sys.path.append('assignment_34')
from cartesian_product import *

def two_variable_function(x,y):
    return (x-1)**2 + (y-1)**3

def grid_search(objective_function, grid_lines):
    cartesian_list = cartesian_product(grid_lines)
    smallest_pair = cartesian_list[0]
    for pair in cartesian_list:
        if objective_function(*pair) < objective_function(*smallest_pair):
            smallest_pair = pair
        else:
            continue
    return smallest_pair

x_lines = [0, 0.25, 0.75]
y_lines = [0.9, 1, 1.1, 1.2]
grid_lines = [x_lines, y_lines]
print("Testing that 'grid_search' works...")
assert grid_search(two_variable_function, grid_lines) == [0.75, 0.9]
print("PASSED")
