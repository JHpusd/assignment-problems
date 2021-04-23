import math
import inspect

class Sudoku():
    def __init__(self, puzzle_dimensions, group_dimensions):
        self.dimensions = puzzle_dimensions.split('x')
        self.dimensions = list(map(int, self.dimensions))
        self.group_dim = group_dimensions.split('x')
        self.group_dim = list(map(int, self.group_dim))
        assert self.dimensions[0] == self.dimensions[1], 'puzzle needs to be square'
        assert self.group_dim[0]*self.group_dim[1]==self.dimensions[0], 'dimensions error'
        self.row_col_sum = sum([i for i in range(1, self.dimensions[0]+1)])
    
    def fit_array(self, arr):
        assert len(arr) == self.dimensions[0], 'number of rows error'
        for row in arr:
            assert len(row) == self.dimensions[1], 'number of columns error'
        all_nums = [num for row in arr for num in row if num != None]
        assert max(all_nums) <= self.dimensions[0], 'max number error'
        assert min(all_nums) > 0, 'min number error'
        self.puzzle = arr

        # making groups
        num_row_groups = math.floor(self.dimensions[0] / self.group_dim[0])
        num_col_groups = math.floor(self.dimensions[1] / self.group_dim[1])
        num_groups = self.dimensions[0]
        groups = []
        row_index = 0
        col_index = 0
        # getting top left grids
        for _ in range(num_row_groups):
            col_index = 0
            for _ in range(num_col_groups):
                groups.append([(row_index, col_index)])
                col_index += self.group_dim[1]
            row_index += self.group_dim[0]
        # rest of groups
        for group in groups:
            top_left = group[0]
            group.remove(top_left)
            for i in range(self.group_dim[0]):
                for j in range(self.group_dim[1]):
                    group.append((top_left[0] + i, top_left[1] + j))
        self.groups = [self.coord_list_to_vals(group) for group in groups]

    def print_puzzle(self):
        print('-----------------')
        row_counter = 1
        col_counter = 1
        for row in self.puzzle:
            if row_counter > self.group_dim[0]:
                print('-----------------')
                row_counter = 1
            print('|', end=' ')
            for item in row:
                if col_counter > self.group_dim[1]:
                    col_counter = 1
                    print('|', end=' ')
                if item == None:
                    print('.', end=' ')
                    col_counter += 1
                    continue
                print(str(item), end=' ')
                col_counter += 1
            col_counter = 1
            print('|')
            row_counter += 1
        print('-----------------')
    
    def get_groups(self, sudoku_square, group_dim):
        side_len = len(sudoku_square)
        # making groups
        num_row_groups = math.floor(side_len / group_dim[0])
        num_col_groups = math.floor(side_len / group_dim[1])
        num_groups = side_len
        groups = []
        row_index = 0
        col_index = 0
        # getting top left grids
        for _ in range(num_row_groups):
            col_index = 0
            for _ in range(num_col_groups):
                groups.append([(row_index, col_index)])
                col_index += group_dim[1]
            row_index += group_dim[0]
        # rest of groups
        for group in groups:
            top_left = group[0]
            group.remove(top_left)
            for i in range(group_dim[0]):
                for j in range(group_dim[1]):
                    group.append((top_left[0] + i, top_left[1] + j))
        for group in groups:
            for i in range(len(group)):
                group[i] = sudoku_square[group[i][0]][group[i][1]]
        return groups
    
    def coord_list_to_vals(self, coord_list):
        return [self.puzzle[coord[0]][coord[1]] for coord in coord_list]
    
    def is_valid(self, puzzle_square=None):
        puzzle = self.puzzle
        dimensions = self.dimensions
        groups = self.groups
        if puzzle_square != None:
            puzzle = puzzle_square
            dimensions = [len(puzzle), len(puzzle[0])]
            groups = self.get_groups(puzzle_square, self.group_dim)
            assert dimensions[0] == dimensions[1], 'wack dimensions on input square'
        n = sum([i for i in range(1, dimensions[0] + 1)])

        for row in puzzle:
            if None not in row and sum(row) != n:
                return False
            else:
                no_none = [i for i in row if i != None]
                if len(set(no_none)) != len(no_none):
                    return False
        
        cols = []
        for col_index in range(len(puzzle[0])):
            cols.append([row[col_index] for row in puzzle])
        for col in cols:
            if None not in col and sum(col) != n:
                return False
            else:
                no_none = [i for i in col if i != None]
                if len(set(no_none)) != len(no_none):
                    return False
        
        for group in groups:
            if None not in group and sum(group) != n:
                return False
            else:
                no_none = [i for i in group if i != None]
                if len(set(no_none)) != len(no_none):
                    return False
        return True
    
    def get_all_puzzle_nums(self):
        result = []
        for row in self.puzzle:
            for item in row:
                if item not in result:
                    result.append(item)
        return result
    
    def square_to_arr(self, square):
        return [item for row in square for item in row]
    
    def arr_to_square(self, arr):
        side_len = int(len(arr) ** 0.5)
        return [arr[i:i+side_len] for i in range(0, len(arr), side_len)]
    
    def arr_to_square_index(self, arr_index, arr, square):
        side_len = len(square)
        i = math.floor(arr_index / side_len)
        j = arr_index % side_len
        return (i, j)

    def fill_in_puzzle(self):
        puzzle_arr = self.square_to_arr(self.puzzle)
        known_indices = [i for i in range(len(puzzle_arr)) if puzzle_arr[i] != None]
        current_index = 0
        max_val = self.dimensions[0]
        increase_index = True

        while None in puzzle_arr or not self.is_valid(self.arr_to_square(puzzle_arr)):
            if current_index in known_indices:
                if increase_index:
                    current_index += 1
                else:
                    current_index -= 1
                continue
            
            if puzzle_arr[current_index] == None:
                puzzle_arr[current_index] = 0
            puzzle_arr[current_index] += 1
            
            if puzzle_arr[current_index] >= max_val+1:
                puzzle_arr[current_index] = None
                current_index -= 1
                increase_index = False
                continue
            
            if self.is_valid(self.arr_to_square(puzzle_arr)):
                current_index += 1
                increase_index = True
        
        self.puzzle = self.arr_to_square(puzzle_arr)

sudoku = Sudoku('6x6', '2x3')
puzzle = [
    [None, None, 4, None, None, None], [None, None, None, 2, 3, None],
    [3, None, None, None, 6, None], [None, 6, None, None, None, 2],
    [None, 2, 1, None, None, None], [None, None, None, 5, None, None]]
'''
correct_puzzle = [
    [1,3,4,5,6,2],
    [5,2,6,4,1,3],
    [6,1,3,2,5,4],
    [2,4,5,1,3,6],
    [4,6,1,3,2,5],
    [3,5,2,6,4,1]]
'''
sudoku.fit_array(puzzle)
sudoku.fill_in_puzzle()
sudoku.print_puzzle()
print(sudoku.is_valid())
