import re
import math

# Opens the data file and extracts the string as list of lines
f = open("input.txt", "r")
data = f.read()
list_lines = data.split('\n')

def find_integers_and_indices(input_string):
    """Finds integers in a string and returns a list fo integers 
    with their associated spans (indices)

    Args:
        input_string (str): string to search through

    Returns:
        (list, list): list of integers, list of asscoiated indices
    """
    pattern = r'\d+'
    matches = re.finditer(pattern, input_string)
    result = [(int(match.group()), (match.start(), match.end())) for match in matches]
    
    return result

def is_part_number(line, upper="", lower=""):
    """Determines if a line has integers which are in "contact" 
    with non integer characters (.) is not considered, e.g.
    467..114..    --> 467 and 35 are part numbers
    ...*......
    ..35..633.

    Args:
        line (_type_):  string to search through
        upper (str, optional): string located above. Defaults to "".
        lower (str, optional): string located below. Defaults to "".

    Returns:
        list[int]: list of part numbers
    """
    part_numbers = []
    num_and_inds = find_integers_and_indices(line)
    for number, inds in num_and_inds:
        min_ind, max_ind = inds
        min_ind -= 1
        max_ind += 1
        if inds[0] == 0:
            min_ind = 0
        if inds[1] == len(line):
            max_ind = len(line)
        str_span = line[min_ind:max_ind] + \
                   upper[min_ind:max_ind] + \
                   lower[min_ind:max_ind]
        char_list = ["*", "@", "#", "/", "%", "$", "=", "-", "+", "&"]
        add_number = 0
        for char in char_list:
            if char in str_span:
                add_number = number
        part_numbers.append(add_number)
    return part_numbers

def find_gear_indices(input_string):
    """Finds the indices associated to (*) characters in a string

    Args:
        input_string (str): string to search through

    Returns:
        list(int): list of indices
    """
    pattern = "\*"
    matches = re.finditer(pattern, input_string)
    result = [match.start() for match in matches]
    
    return result

def is_valid_gear(line, upper="", lower=""):
    """Determines if the gears in line are valid, i.e. they are 
    touching two different integers, and if they are returns their
    gear ratio (product of the two integers) e.g.
    467..114..   -->   the gear is valid and the function returns 
    ...*......         467*35
    ..35..633.

    Args:
        line (str): string to search through
        upper (str, optional): string located above. Defaults to "".
        lower (str, optional): string located below. Defaults to "".

    Returns:
        list(int): list of gear ratios
    """
    gear_ratios = [0]
    gear_indices = find_gear_indices(line)
    current_ints_inds = find_integers_and_indices(line) + \
                        find_integers_and_indices(upper) + \
                        find_integers_and_indices(lower)
    for gear_index in gear_indices:
        neighbours = []
        print(current_ints_inds)
        for int, inds in current_ints_inds:
            if gear_index in range(inds[0], inds[1])\
            or gear_index-1 in range(inds[0], inds[1])\
            or gear_index+1 in range(inds[0], inds[1]):
                neighbours.append(int)
        if len(neighbours) == 2:
            gear_ratios.append(math.prod(neighbours))
    return gear_ratios

numbers = []
gears = []
for i, line in enumerate(list_lines):
    if i == 0:
        numbers.append(sum(is_part_number(line, list_lines[i+1])))
        gears.append(sum(is_valid_gear(line, list_lines[i+1])))
    elif i == len(list_lines)-1:
        numbers.append(sum(is_part_number(line, list_lines[i-1])))
        gears.append(sum(is_valid_gear(line, list_lines[i-1])))
    else:
        numbers.append(sum(is_part_number(line, list_lines[i-1], list_lines[i+1])))
        gears.append(sum(is_valid_gear(line, list_lines[i-1], list_lines[i+1])))
    
print(sum(numbers))
print(sum(gears))

