"""Project 3 - Calcudoku Tests
CPE 101
Section: 3 & 7
Name: Amy Ru
Cal Poly User: amru
"""PV 
import calcudoku

# no tests for main(), get_num_cages(), get_cage_info()

test_cages = [[4, 3, 0, 1, 6], [8, 3, 2, 7, 12], [14, 3, 3, 4, 8], \
    [15, 4, 5, 10, 11, 15], [14, 6, 9, 13, 14, 18, 19, 24], \
        [11, 3, 16, 20, 21], [9, 3, 17, 22, 23]]

placebo_cages = [[0, 3, 0, 1, 0], [0, 3, 2, 7, 0], [0, 3, 3, 4, 0], \
    [0, 4, 5, 10, 11, 0], [0, 6, 9, 13, 14, 18, 19, 0], \
        [0, 3, 16, 20, 0], [0, 3, 17, 22, 0]]

test_grid = [[1,5,2,3,4],
            [5,3,1,4,2],
            [2,4,3,5,1],
            [3,2,4,1,5],
            [4,1,5,2,3]]

placebo_grid = [[1,5,2,3,2],
            [5,2,1,3,2],
            [3,4,3,5,2],
            [2,2,4,3,5],
            [4,3,2,2,3]]

placebo_grid2 = [[1,5,2,3,4],
            [5,3,1,3,2],
            [3,4,3,5,3],
            [3,2,4,3,5],
            [4,3,5,2,3]]

# testing validate_all(grid: list, cages: list) -> bool:
assert calcudoku.validate_all(test_grid, test_cages) == True
assert calcudoku.validate_all(placebo_grid2, placebo_cages) == False
assert calcudoku.validate_all(placebo_grid, test_cages) == False

# testing validate_rows(grid: list) -> bool:
assert calcudoku.validate_rows(test_grid) == True
assert calcudoku.validate_rows(placebo_grid) == False
assert calcudoku.validate_rows(placebo_grid2) == False

# testing validate_cols(grid: list) -> bool:
assert calcudoku.validate_cols(test_grid) == True 
assert calcudoku.validate_cols(placebo_grid) == False
assert calcudoku.validate_cols(placebo_grid2) == False

# testing validate_cages(grid: list, cages: list) -> bool:
assert calcudoku.validate_cages(test_grid, test_cages) == True
assert calcudoku.validate_cages(placebo_grid, test_cages) == False
assert calcudoku.validate_cages(placebo_grid2, test_cages) == False