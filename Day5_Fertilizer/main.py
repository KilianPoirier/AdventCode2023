import re
import math
from copy import copy
import gc
gc.collect()

# Opens the data file and extracts the string as list of lines
f = open("input.txt", "r")
data = f.read()
list_lines = data.split('\n\n')

pattern = r'\d+'
numbers = [int(match.group()) for match in re.finditer(pattern, list_lines[0])]
nums = numbers[:4:2]
lengths = numbers[1:4:2]
seeds = []
for i, num in enumerate(nums):
    seeds.extend(range(num, num+lengths[i]))
# seeds = [i for num, length in numbers[::2] for i in range(num, num+length)]

def apply_map(value, dest_start, source_start, length):
    if value >= source_start and value < source_start+length:
        update = True
        return (value + dest_start - source_start, update)
    else:
        update = False
        return (value, update)
    
def convert_seed_to_location(seed, map_strings):
    for a_to_b in map_strings:
        maps = [[int(match.group()) for match in re.finditer(pattern, maps)] for maps in a_to_b.split('\n')[1:]]
        update = False
        for map in maps:
            if not update:
                seed, update = apply_map(seed, *map)
    return seed

def find_lowest_location(seeds, map_strings, lowest_location=float('inf')):
    # lowest_location = float('inf')
    for seed in seeds:
        location = convert_seed_to_location(seed, map_strings)
        lowest_location = min(lowest_location, location)
    return lowest_location

print(find_lowest_location(seeds, list_lines[1:]))