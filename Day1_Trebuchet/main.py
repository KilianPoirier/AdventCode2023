# Opens the data file and extracts the string as list of lines
f = open("input.txt", "r")
data = f.read()
list_lines = data.split('\n')

def is_following_string_a_digit(input_str):
    """Finds a string associated to a digit and returns its integer value 
    if the given string contains one, otherwise returns None, e.g. 
    "eth3e6three"    -->    None
    "onejd9e4"       -->    1

    Args:
        input_str (str): string to search through

    Returns:
        int or None: value fo the digit found if there is one, otherwise None
    """
    digit_str_list = ["one",
                      "two",
                      "three",
                      "four",
                      "five",
                      "six",
                      "seven",
                      "eight",
                      "nine"]
    digit_value = None
    for index, digit in enumerate(digit_str_list):
        if len(input_str) >= len(digit):
            if input_str[:len(digit)] == digit:
                digit_value = index + 1

    return digit_value

def is_following_string_a_reversed_digit(input_str):
    """Finds a string associated to a reversed digit and returns its 
    integer value if the given string contains one, otherwise returns None, e.g. 
    "eth3e6eerht"    -->    None
    "enojd9e4"       -->    1

    Args:
        input_str (str): string to search through

    Returns:
        int or None: value fo the digit found if there is one, otherwise None
    """
    digit_str_list = ["eno",
                      "owt",
                      "eerht",
                      "ruof",
                      "evif",
                      "xis",
                      "neves",
                      "thgie",
                      "enin"]
    digit_value = None
    for index, digit in enumerate(digit_str_list):
        if len(input_str) >= len(digit):
            if input_str[:len(digit)] == digit:
                digit_value = index + 1

    return digit_value

def find_calibration_values(line_input):
    """This function finds the calibration value which is given 
    by the first and the last digit of the string, e.g. 
    1abc2          -->    12
    pqr3stu8vwx    -->    38
    a1b2c3d4e5f    -->    15
    treb7uchet     -->    77

    It should also be able to detect digits spelled out in letters, e.g.
    two1nine       -->    29
    eightwothree   -->    83

    Args:
        line_input (str): input string corresponding to one line of the text

    Returns:
        int: Calibration value that is included in the input string
    """
    first_digit = None
    second_digit = None
    reversed_line_input = line_input[::-1]
    # Go through the string from the left to find the first digit
    for i in range(len(line_input)):
        if first_digit == None:
            if str.isdigit(line_input[i]):
                first_digit = int(line_input[i])
            elif is_following_string_a_digit(line_input[i:]):
                first_digit = is_following_string_a_digit(line_input[i:])
        if second_digit == None:
            if str.isdigit(reversed_line_input[i]):
                second_digit = int(reversed_line_input[i])
            elif is_following_string_a_reversed_digit(reversed_line_input[i:]):
                second_digit = is_following_string_a_reversed_digit(reversed_line_input[i:])

    calibration_value = first_digit * 10 + second_digit

    return calibration_value


sum = 0
for line in list_lines:
    sum += find_calibration_values(line)

print(sum)