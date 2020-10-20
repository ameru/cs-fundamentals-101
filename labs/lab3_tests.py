import lab3

# testing max_of_two()
assert lab3.max_of_two(100, 50) == 100
assert lab3.max_of_two(1, 1) == 1
assert lab3.max_of_two(0, 200) == 200

# testing max_of_three()
assert lab3.max_of_three(1, 2, 3) == 3
assert lab3.max_of_three(3, 14, 9) == 14
assert lab3.max_of_three(10, 0, 0) == 10

# testing mul()
assert lab3.mul(1, 45) == 45
assert lab3.mul(33, 3) == 99
assert lab3.mul(0, 13) == 0

# testing exp()
assert lab3.exp(2, 2) == 4
assert lab3.exp(60, 0) == 1
assert lab3.exp(3, 3) == 27
