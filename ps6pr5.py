#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# 2-D Lists
#
# Computer Science 111
# 

import random

def create_grid(num_rows, num_cols):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = []
    
    for r in range(num_rows):
        row = [0] * num_cols     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line.
        input: grid is a 2-D list
    """
    num_rows = len(grid)
    for r in range(num_rows):
        if r == 0:
            print('[', end='')
        else:
            print(' ', end='')
        if r < num_rows - 1:
            print(str(grid[r]) + ',')
        else:
            print(str(grid[r]) + ']')

def random_grid(num_rows, num_cols):
    """ creates and returns a 2-D list with the specified dimensions
        in which each cell is assigned a random integer from 0-9.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = create_grid(num_rows, num_cols)

    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = random.choice(range(10))
            
    return grid

def row_index_grid(num_rows, num_cols):
    '''returns a 2-D list where each element in a list (row) is the index of its row
        inputs: num_rows and num_cols are non-negative integers'''
        
    grid = create_grid(num_rows, num_cols)
    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c]= r
            
    return grid

def num_between(grid, n1, n2):
    '''returns the number of values in the list grid that is between or equals n1 and n2
        inputs: n2 and n1 are numbers (n2>n1), grid is a 2-D list of integers'''
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] >= n1 and grid[i][j] <= n2:
                count +=1
    return count


def copy(grid):
    '''takes in a 2-D list, grid, and creates/returns a new list that is a deep copy of grid'''
    row_num = len(grid)
    col_num = len(grid[0])
    new = create_grid(row_num, col_num)
    
    for r in range(row_num):
        for c in range(col_num):
            new[r][c]=grid[r][c]
    return new

def double_with_cap(grid, cap):
    '''takes in a 2-D list of ints, grid, and an int, cap, and doubles each element in grid, unless
    doubling that element would make it greater than the cap, in that case cap replaces that element'''
    row_num = len(grid)
    col_num = len(grid[0])
    
    for r in range(row_num):
        for c in range(col_num):
            if grid[r][c]*2 <= cap:
                grid[r][c] *= 2
            else:
                grid[r][c] = cap
                
def sum_evens_in_col(grid, colnum):
    '''takes in a 2-D list of ints, grid, and a int, colnum, and returns the sum of each number in
    the column of grid's index at colnum'''
    row_num = len(grid)
    sum = 0
    
    for r in range(row_num):
        for c in range(colnum,colnum+1):
            if grid[r][c] % 2 == 0:
                sum += grid[r][c]
    
    return sum
    
            
    
    
                
    