# alternative way to import: from lab2 import *
# for indiv funcs: from lab2 import print_hello
# get_numbers no tests needed
# other funcs need 3 tests each

import lab2

# testing print_hello()
assert lab2.print_hello("Amy") == "Hello Amy!"

# testing cube()
assert lab2.cube(2) == 8
assert lab2.cube(3) == 27
assert lab2.cube(10) == 1000

# testing get_hypotenuse()
assert lab2.get_hypotenuse(0, 0) == 0
assert lab2.get_hypotenuse(1, 1) == 2 ** (1/2)
assert lab2.get_hypotenuse(3, 4) == 5

# testing do_math()
assert lab2.do_math(2, 1) == 4
assert lab2.do_math(5, 0) == 7.5
assert lab2.do_math(1, 4) == 9.5

# testing is_positive()
assert lab2.is_positive(0) == False
assert lab2.is_positive(-693) == False
assert lab2.is_positive(20000) == True

# testing both_positive()
assert lab2.both_positive(123, 456) == True
assert lab2.both_positive(0, 789) == False
assert lab2.both_positive(-147, -369) == False
