"""Project 2 - Word Search
CPE 101
Section: 3 & 7
Name: Amy Ru
Cal Poly User: amru
"""

def main():
    string = input()
    word = input().strip("/n") #strip newsline
    counter = word.count("")

    for i in range(counter + 1):
        a = 0   #initiate x coord constraints
        b = 10  #initiate y coord constraints
        counter = word.find(" ")
        column = 0
        transpose_string = 0
        word_found = 0
        finished = 0

        if counter == -1:
            end_word = word[0:len(word)]
        else:
            end_word = word[0:counter]

        for j in range(10):
            if finished == 0:
                position = ""
                puzzle = string[a:b]

            find_word(search_forward)
            find_word(search_backward)
            find_word(search_up)
            find_word(search_down)

        if (word_found != 0):
            row = int(a / 10)

            if word_found == 2:
                print(end_word + ": " + position + " row: " + str(column) \
                    + " col: " + str(transpose_string))
            elif word_found == 1:
                print(end_word + ": " + position + " row: " + str(row) \
                    + " col: " + str(column))
            
            finished = 1

            a += 10
            b += 10
            transpose_string += 1  

    if finished == 0:
        print(end_word + ": word not found")  

    word = word[(counter+1):len(word)]

def reverse_string(string: str) -> str:
    """ Returns the reverse of the input string.
    Arguments:
        string (str): user input of a string
    Returns:
        str: returns the string that is reverse of input string
    """
    for i in range(len(string)):
        string_rev = string[::1]
    return string_rev

def transpose_string(string: str, row_len: int) -> str:
    """ Returns a transposition of input string
    Arguments:
        string (str): user input of string
        row_len (int): length of characters in given row
    Returns:
        str: String with its characters shifted around
    """
    input_string = ""
    for i in range (row_len):
        string_index = string[0]
        input_string += string_index
        string[0] += row_len
    return input_string

def find_word(puzzle: str, word: str, row_len: int) -> str:
    """ Searches the puzzle for the given word (in any direction).
    Arguments:
        puzzle (str): character that is either lowercase or uppercase
        word (str): user input of string
        row_len (int): integer representing the row word is in
    Returns:
        str: returns a string containing search result to be printed in main()
    """
    string = ""

    if -1 != puzzle.find(word):
        search_forward = find_word(puzzle, word, 10)
        position = "(FORWARD)"
        word_found += 1

    search_backward = reverse_string(puzzle, word, 10)
    if (-1 != find_word(reverse_string, word)) and (column == 0):
        column = find_word(reverse_string, word)
        column = 9 - column
        position = "(BACKWARD)"
        word_found += 1

    search_down = transpose_string(puzzle, word, 10)
    if (-1 != find_word(transpose_string, word)) and (column == 0):
        column = find_word(transpose_string, word)
        position = "(DOWN)"
        word_found += 2

    search_up = reverse_string((transpose_string(puzzle, word, 10)))
    if (-1 != find_word(transpose_string, word)) and (column == 0):
        column = find_word(transpose_string, word)
        column = 9 - column
        position = "(UP)"
        word_found += 2

if __name__ == "__main__":
    main()