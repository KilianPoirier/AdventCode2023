import re
from operator import mul
from functools import reduce

# Opens the data file and extracts the string as list of lines
f = open("input.txt", "r")
data = f.read()
list_lines = data.split('\n')

def is_game_possible(line_input):
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14
    game_str, colors_str = line_input.split(": ")
    game_id = int(re.search(r'\d+', game_str).group())
    for game in colors_str.split("; "):
        for color_number in game.split(", "):
            number = int(re.search(r'\d+', color_number).group())
            if "red" in color_number and number > MAX_RED:
                game_id = 0
            elif "green" in color_number and number > MAX_GREEN:
                game_id = 0
            elif "blue" in color_number and number > MAX_BLUE:
                game_id = 0

    return game_id

def find_minimum_set_size(line_input):
    _ , colors_str = line_input.split(": ")
    min_red, min_green, min_blue = 1, 1, 1
    for game in colors_str.split("; "):
        for color_number in game.split(", "):
            number = int(re.search(r'\d+', color_number).group())
            if "red" in color_number and number > min_red:
                min_red = number
            elif "green" in color_number and number > min_green:
                min_green = number
            elif "blue" in color_number and number > min_blue:
                min_blue = number
    minimum_set_size = [min_red, min_green, min_blue]
    return minimum_set_size

def calc_set_power(set):
    return reduce(mul, set, 1)

game_ids = [is_game_possible(line) for line in list_lines]
print(sum(game_ids))

min_set_list = [calc_set_power(find_minimum_set_size(line)) for line in list_lines]
print(sum(min_set_list))