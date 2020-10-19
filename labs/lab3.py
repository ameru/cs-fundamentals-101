def max_of_two(x: int, y: int) -> int:
""" find the larger number of two integers
Arguments:
    x (int): an integer
    y (int): another integer
Returns:
    int: the bigger number of two integers
""" 
    if x > y:
        return x
    else:
        return y

def max_of_three(x: int, y: int, z: int) -> int:
""" find the largest number of three integers
Arguments:
    x (int): an integer
    y (int): another integer
    z (int): a third integer
Returns:
    int: the largest number of three integers
""" 
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    else:
        return z

def mul(x: int, y: int) -> int:
""" performs multiplication without using * operator
Arguments:
    x (int): an integer
    y (int): another integer
Returns:
    int: the product of two integers
"""
    n = 0
    sum = 0
    while n < y:
        sum = sum + x 
        n += 1
    return sum

def exp(x: int, y: int) -> int:
""" performs exponentiation without using the ** operator
Arguments:
    x (int): an integer
    y (int): another integer
Returns:
    int: x integer to the power of y integer
"""
    n = 0
    product = 1
    while n < y:
        product = mul(product, x)
        n += 1
    return product
