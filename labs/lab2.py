# From lab: use 4 spaces for indentation, not tabs
# put one argument per line
# docstrings are just extended comments (like // and /* */)

def print_hello(name: str) -> str:
    result = "Hello " + name + "!"
    print(result)
    return result

def get_numbers() -> int:
    input_1 = int(input("Enter a number: "))
    input_2 = int(input("Enter another number: "))
    return input_1 + input_2

def cube(x: int) -> int:
    return int(x**3)

def get_hypotenuse(a: int, b: int) -> float:
    return ((a**2) + (b**2)) ** (1/2)

def do_math(x: int,y: int) -> float:
    return (((3*(x**2)) + (4*y)) / (2*x))

def is_positive(x: int) -> int:
    return x > 0

def both_positive(x: int, y: int) -> int:
    return is_positive(x) and is_positive(y)
    
