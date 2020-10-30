# Map Pattern
# Implement one func using list comprehension, one for loop, one while loop

def square_all(int_list: list) -> list:
    """ Returns a list of the square of each value in the input list.
    Arguments:
        int_list (list): user input list
    Returns:
        list: list that contains the square of each value
    """
    new_list = []
    new_list = [(int_list[i] ** 2) for i in range(len(int_list))]
    return new_list

def add_n_all(int_list: list, n: int) -> list:
    """ Returns a list with n added to each element in the input list.
    Arguments:
        int_list (list): user input list
        n (int): given integer
    Returns:
        list: list containing n added to all inputs
    """
    new_list = []
    i = 0
    while i != len(int_list):
        new_list.append(int_list[i] + n)
        i += 1
    return new_list

def is_even_all(int_list: list) -> list:
    """ Returns a list containing boolean values representing whether each
        corresponding integer in the input list is even or odd.
    Argumnets:
        int_list (list): user input list
    Returns:
        list: returns True if even and returns False if odd
    """
    new_list = []
    for i in range(len(int_list)):
        if int_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list

# Filter Pattern
# Implement one func using list comprehension. one for loop, one while loop

def are_positive(int_list: list) -> list:
    """ Returns a list of all positive values in the input list.
        my_str (str): given string
    Arguments:
        int_list (list): user input list
    Returns:
        list: list containing positive values from input
    """
    new_list = []
    for i in range(len(int_list)):
        if (int_list[i] > 0):
            new_list.append(int_list[i])
    return new_list

def are_greater_than_n(int_list: list, n: int) -> list:
    """ Returns a list of all integers in the input list that are greater than
        the n parameter.
    Arguments:
        int_list (list): user input list
        n (int): given integer
    Returns:
        list: list containing integers from input > n
    """
    new_list = []
    for i in range(len(int_list)):
        if int_list[i] > n:
            new_list.append(int_list[i])
    return new_list

def are_divisible_by_n(int_list: list, n: int) -> list:
    """ Returns all integers in the input list that are divisible by the n
        parameter.
    Arguments:
        int_list (list): user input list
        n (int): given integer
    Returns:
        list: all integers in list divisible by n.
    """
    new_list = []
    i = 0
    while i != len(int_list):
        if(int_list[i] % n) == 0:
            new_list.append(int_list[i])
        i += 1
    return new_list

# Reduce Pattern
# Implement one func using a for loop and one using a while loop

def sum_101(my_list: list) -> list:
    """ Returns the sum of all values in the input list.
    Arguments:
        my_list (list): given list of integers
    Returns:
        list: integer containing sum of all values in list.
    """
    new_list = 0
    for i in range(len(my_list)):
        new_list += my_list[i]
    return new_list
 
def index_of_smallest(my_list: list) -> list:
    """ Returns index of the smallest value in the input list. If list is
        empty, then the function returns -1. If there is more than one smallest
        values, return the index of the first occurrence of it (left to right).
    Arguments:
        my_str (str): given string
        old (str): a character that will be replaced in my_str
        new (str): a character that will replace another one in my_str
    Returns:
        list: list containing index(es) of smallest value.
    """
    new_list = []
    accum = 0
    while accum != len(my_list):
        new_list.append(my_list[accum])
        accum += 1
    accum = 0
    if len(my_list) == 0:
        return []
    while (accum + 1) != len(my_list):
        if my_list[accum] < my_list[accum + 1]:
            my_list.pop(accum + 1)
        elif my_list[accum] > my_list[accum + 1]:
            my_list.pop(accum)
    return new_list.index(my_list[accum])
