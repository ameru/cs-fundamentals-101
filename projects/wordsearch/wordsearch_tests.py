"""Project 2 Tests - Word Search
CPE 101
Section: 3 & 7
Name: Amy Ru
Cal Poly User: amru
"""

import wordsearch

# testing reverse_string(string: str) -> str:
test1 = 'CALPOLY'
test2 = 'AMY'
test3 = 'PYTHON'
assert wordsearch.reverse_string(test1) == 'YLOPLAC'
assert wordsearch.reverse_string(test2) == 'YMA'
assert wordsearch.reverse_string(test3) == 'NOHTYP'

#testing transpose_string(string: str, row_len: int) -> str:
test4 = 'ABCGITHUBXYZ'
test5 = 'TIKTOKTAK'
test6 = 'CATZCOTZCUTZ'
assert wordsearch.transpose_string(test4, 5, 1) == 'BHZ'
assert wordsearch.transpose_string(test5, 3, 0) == 'TTT'
assert wordsearch.transpose_string(test6, 4, 0) == 'ZZZ'

#testing find_word(puzzle: str, word: str, row_len: int) -> str:
wordsearch1 = 'javajavajavajavajavajavajavajavajavajavajavajavajavajava'
wordsearch2 = 'codecodecodecodecodecodecodecodecodecodecodecodecodecode'
wordsearch3 = 'imcryingimcryingimcryingimcryingimcryingimcryingimcrying'
test7 = 'java' 
test8 = 'code'
test9 = 'happy'
assert wordsearch.find_word(wordsearch1, test7) == 0
assert wordsearch.find_word(wordsearch2, test8) == 0
assert wordsearch.find_word(wordsearch3, test9) == -1

# no tests needed for main()