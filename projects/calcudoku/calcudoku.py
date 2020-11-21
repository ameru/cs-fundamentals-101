""" Project 3 - Calcudoku
CPE 101
Section: 3 & 7
Name: Amy Ru
Cal Poly User: amru
"""
# OO Hints:
# row = index // dimension (floor division)
# col = index % dimension (modulo)
# cell = grid[row][col]
# cell = grid[num // dim][num % dim]

def main() -> None:
    # store the data from the puzzle input file in a 2D list of ints
    # create a 5x5 grid using a 2D list and fill it with zeros
    # only one while loop is recommended to validly populate every cell in the
    # grid

    cages = get_num_cages()
    print(cages)
    cages = get_cage_info(num)
    print(cages)
    
    grid = []
    i = 0

    while i < 25:
        grid[i // 5][i % 5] += 1
        if grid[i // 5][i % 5] < 6 and validate_all(grid, cages):
            i += 1
        elif grid[i // 5][i % 5] < 5:
            continue
        else:
            grid[i // 5][i % 5] = 0
            i -= 1
    print_grid(grid)

def get_num_cages() -> int:
    """ Asks user to input num of cages and returns num of cages.
    Arguments:
        None
    Returns:
        int: int value representing number of cages
    """
    number_of_cages = str(input("Number of cages: "))
    if number_of_cages.isdigit():
        return int(number_of_cages)

def get_cage_info(num: int) -> list:
    """ Asks for info, where num of lists is num, and each list contains info
        about a cage.
    Arguments:
        num (int): number of the lists given by users
    Returns:
        list: returns a list of lists
    """    
    # use input() to ask the user to enter info
    # you may have to repeat asking for info num amount of times
    # use split() func to split a string into a list of strings at a space
    # (ex: elements = string.split())
    # user list comprehensions to convert a list of strings into a list of int
    grid = []
    for i in range(num):
        calcudoku_input = input("Please enter the cage grids: ") # '1','5','2'
        grid.append(calcudoku_input) # add input to list
        calcudoku_input.split()  # .split ['1','5','2']
        cages = list(map(int, num))
    return cages

def validate_all(grid: list, cages: list) -> bool:
    """ Returns boolean value for all 3 validation functions.
    Arguments:
        grid (list): list of values in 5x5 grid
        cages (list): list of values in each calcudoku cage
    Returns:
        boolean: returns True if all 3 functions return True and else False
    """    
    return validate_cages(grid, cages) and validate_rows(grid) \
    and validate_cols(grid) 

def validate_rows(grid: list) -> bool:
    """ Returns boolean value for checking duplicate values in rows.
    Arguments:
        grid (list): list of values in 5x5 grid
    Returns:
        boolean: returns True if all rows contain no duplicates postive numbers,
        else returns False
    """    
    for i in range(5):
        for j in range(5):
            if grid[i][j] > 0 and grid[i].count(grid[i][j]) > 1:
                return False
    return True

def validate_cols(grid: list) -> bool:
    """ Returns boolean value for checking duplicate values in columns.
    Arguments:
        grid (list): list of values in 5x5 grid
    Returns:
        bool: return True if all columns contain no duplicate positive numbers,
        else return False
    """   
    # recommended that you transpose the grid (convert its rows to columns and
    # columns to rows) and pass this transposition to validate_rows to reuse
    # you existing code
    grid = transpose_grid(grid)
    validate_rows(grid)

def validate_cages(grid: list, cages: list) -> bool:
    """ Returns boolean value for checking matchup for cage value and current
    cage sum.
    Arguments:
        grid (list): list of values in 5x5 grid
        cages (list): list of values in each calcudoku cage
    Returns:
        bool: returns True if sum of values in full cage equals required sum or
        if the sum of values in a partially populated cage is less than the 
        required sum, else returns False
    """    
    for i in range(len(cages)):
        cage_goal = cages[i][0]
        cage_sum = 0
        counter_0 = 0
        grid = []

        for j in range(2, len(cages[i])):
            grid.append(cages[i][j])
        for k in range(len(grid)):
            cage_sum += grid[grid[k] // 5][grid[k] % 5]
            if grid[grid[k] // 5][grid[k] % 5] == 0:
                counter_0 += 1
        if cage_sum != cage_goal and counter_0 == 0:
            return False
        if cage_sum >= cage_goal and counter_0 == 1:
            return False
    return True

#####

# Helper functions you might want to create:

def transpose_grid(grid: list) -> list:
    """Transposes a grid.
    Arguments:
        grid (list): a grid
    Returns:
        list: a list of lists which is a transposed version of the grid.
    """
    t_grid = []
    for i in range(5):
        new_grid = []
        for j in range(5):
            new_grid.append(grid[j][i])
        t_grid.append(new_grid)

def create_grid(dim: int) -> list:
    """Creates a grid of dim * dim.
    Arguments:
        dim (int): the dimension
    Returns:
        list: a list of lists of 0s.
    """
    grid = []
    for i in range(5):
        grid.append([dim]*5)
    return grid

def print_grid(grid: list) -> list:
    """Prints the grid.
    Arguments:
        grid (list): a list of lists
    """
    for i in range(5):
        print(str(grid[i][0]) + " " + str(grid[i][1]) + " " + str(grid[i][2]) \
            + " " + str(grid[i][3]) + " " + str(grid[i][4]))


if __name__ == "__main__":
    main()
