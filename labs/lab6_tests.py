import lab6

# testing square_all(int_list) -> list:
assert lab6.square_all([1, 2, 3]) == [1, 4, 9]
assert lab6.square_all([0]) == [0]
assert lab6.square_all([-5, -3, -10]) == [25, 9, 100]

# testing add_n_all(int_list, n) -> list:
assert lab6.add_n_all([108, 654, 357], 2) == [110, 656, 359]
assert lab6.add_n_all([-32, -85, 0], -10) == [-42, -95, -10]
assert lab6.add_n_all([0], 0) == [0]

# testing is_even_all(int_list) -> list:
assert lab6.is_even_all([210, 369, 114]) == [True, False, True]
assert lab6.is_even_all([123, 456, 789]) == [False, True, False]
assert lab6.is_even_all([102]) == [True]

# testing are_positive(int_list) -> list:
assert lab6.are_positive([102, -369, 454]) == [102, 454]
assert lab6.are_positive([64, 10, 2]) == [64, 10, 2]
assert lab6.are_positive([-1, -36, -5889]) == []

# testing are_greater_than_n(int_list, n) -> list:
assert lab6.are_greater_than_n([123, 456, 789], 1000) == []
assert lab6.are_greater_than_n([100, 200, 300], 0) == [100, 200, 300]
assert lab6.are_greater_than_n([156, 345], 200) == [345]

# testing are_divisible_by_n(int_list, n) -> list:
assert lab6.are_divisible_by_n([100, 64], 10) == [100]
assert lab6.are_divisible_by_n([152, 147, 3], 2) == [152]
assert lab6.are_divisible_by_n([357, 159, 852], 10) == []

# testing sum_101(my_list) -> list:
assert lab6.sum_101([1, 2, 3, 4, 5]) == 15
assert lab6.sum_101([30, 50, 60]) == 140
assert lab6.sum_101([-89, 89]) == 0

# testing index_of_smallest(my_list) -> list:
assert lab6.index_of_smallest([1, 2, 3, 4, 5]) == 0
assert lab6.index_of_smallest([9, 8, 7, 6]) == 3
assert lab6.index_of_smallest([50, 36, 91, 400]) == 1
