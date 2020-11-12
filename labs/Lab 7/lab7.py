"""Lab 7
CPE 101
Section: 3 & 7
Name: Amy Ru
Cal Poly User: amru
"""

# test1.out is for test1.in without -s option.
# test2.out is for test2.in without -s option.
# test3.out is for test1.in with -s option.
# test4.out is for test2.in with -s option.

import sys
arguments = sys.argv

# HELPER FUNCTIONS

def validate_output(array):
    """ Checks to cast output type to int or float.
    Arguments:
        array (list): an array of integers or floats.
    Returns:
        list or float.
    """
    output = [0, 0, 0, 0]
    for i in range(len(array)):
        try:
            int(array[i])
            output[0] += 1
            output[3] += int(array[i])
        except ValueError:
            try:
                float(array[i])
                output[1] += 1
                output[3] += float(array[i])
            except ValueError:
                output[2] += 1
    return output

def split(array):
    """ Splits output from file to list.
    Arguments:
        array (list): an array of integers or floats.
    Returns:
        list or float.
    """
    new_array = []
    file_array = []
    for i in range(len(array)):
        new_array.append(array[i].split("\t"))
    for lists in new_array:
        for output in lists:
            file_array.append(output)
    return file_array

def strip(array):
    """ Strips list of trailing whitespace or newline characters.
    Arguments:
        array (list): an array of integers or floats.
    Returns:
        list or float.
    """
    for i in range(len(array)):
        array[i] = array[i].strip()
    return array

def print_file(arguments, output):
    """ Prints the file.
    Arguments:
        Arguments (str): sys args provided in Arguments.
        output (integer): value of integer in list.
    Returns:
        N/A
    """
    print("int: " + str(output[0]))
    print("float: " + str(output[1]))
    print("other: " + str(output[2]))
    if '-s' in arguments:
        print("sum: " + str(output[3]))

# ASSIGNMENT FUNCTIONS

def num_of_args():
    """ Validates correct amount of Arguments was inputted.
    Arguments:
        N/A
    Returns:
        (str): name of file.
    """
    if  len(arguments) > 3 or len(arguments) < 2:
        print("Usage: [-s] infile_name outfile_name")
        sys.exit()
    elif len(arguments) == 2:
        file_name = arguments[1]
    elif len(arguments) == 3:
        if '-s' not in arguments:
            print("Usage: [-s] infile_name outfile_name")
            sys.exit()
        elif arguments[1] == '-s':
            file_name = arguments[2]
        elif arguments[2] == '-s':
            file_name = arguments[1]
    return file_name

def read_file(file_name):
    """ Reads the file and creates text list.
    Arguments:
        file_name (str): name of file.
    Returns:
        int: text value.
    """
    try:
        file_value = open(file_name, 'r')
        text = file_value.readlines()
        text = strip(text)
        text = split(text)
    except PermissionError or FileNotFoundError:
        print("Unable to open " + file_name)
        sys.exit()
    return text

def main():
    """ Runs main function.
    Arguments:
        N/A
    Returns:
        two required Arguments, one optional -s argument.
    """
    file_name = num_of_args()
    text = read_file(file_name)
    output = validate_output(text)
    print_file(arguments, output)

if __name__ == '__main__':
    main()
