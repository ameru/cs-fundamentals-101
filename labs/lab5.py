def is_lower(char) -> bool:
    """ Determines if given character is lowercase.
    Arguments:
        char (bool): character that is either lowercase or uppercase
    Returns:
        boolean: True if lowercase, False if other
    """
    if char >= 'a' and char <= 'z':
        return True 
    else:
        return False

def char_rot_13(char) -> str:
    """ Returns a caesar-cypher encryption ROT-13 of a given character.
    Arguments:
        char (str): character that will be replaced with ROT-13 character.
    Returns:
        str: Character of the alphabet 13 places forward or backward of given
        character
    """
    
    if char.islower():
        return chr((((ord(char) - 97) + 13) % 26) + 97)
    elif char.isupper():
        return chr((((ord(char) - 65) + 13) % 26) + 65)
    else:
        return char
     
# this only works on characters of the alphabet
# lowercase -> lowercase, uppercase -> uppercase
# others remain unchanged
# may use functions: str.isalpha(), str.islower(), str.isupper()

def str_rot_13(my_str) -> str:
    """ Returns a caesar-cypher encryption ROT-13 of a given string.
    Arguments:
        my_str (str): string that will be replaced with ROT-13 string.
    Returns:
        str: String of the alphabet 13 places forward or backward of given
        string
    """
    word = ''
    for i in range(len(my_str)):
        word += char_rot_13(my_str[i])
    return word


def str_translate(my_str, old, new) -> str:
    """ Replaces each "old" character in "my_str" with a "new" character.
    Arguments:
        my_str (str): given string
        old (str): a character that will be replaced in my_str
        new (str): a character that will replace another one in my_str
    Returns:
        str: new string with every "old" character replaced with "new"
    """
    word = ''
    for i in range(len(my_str)):
        if my_str[i] != old:
            word += my_str[i]
        else:
            word += new
    return word 
    
