import lab5

# testing is_lower(char) -> bool:
assert lab5.is_lower('a') == True
assert lab5.is_lower('B') == False
assert lab5.is_lower('%') == False

# testing char_rot_13(char) -> str:
assert lab5.char_rot_13('a') == 'n'
assert lab5.char_rot_13('Z') == 'M'
assert lab5.char_rot_13('I') == 'V'

# testing str_rot_13(my_str) -> str:
assert lab5.str_rot_13('Amy') == 'Nzl'
assert lab5.str_rot_13('toshi') == 'gbfuv'
assert lab5.str_rot_13('cpe101') == 'pcr101'

# testing str_translate(my_str, old, new) -> str:
assert lab5.str_translate('pizza','z','t') == 'pitta'
assert lab5.str_translate('uwuwu','u','o') == 'owowo'
assert lab5.str_translate('computer','p','m') == 'commuter'
