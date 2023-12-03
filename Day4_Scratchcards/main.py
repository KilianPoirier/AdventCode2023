import re
import math

# Opens the data file and extracts the string as list of lines
f = open("input.txt", "r")
data = f.read()
list_lines = data.split('\n')

def count_winning_numbers(line):
    """Counts the number of matching integers between the left and 
    right part of the string, separated by |, and returns that number, e.g.
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 --> 4 

    Args:
        line (str): string to search through

    Returns:
        int: number of matching integers
    """
    _, my_nums, winning_nums = re.split(': |\| ', line)
    pattern = r'\d+'
    my_nums = [match.group() for match in re.finditer(pattern, my_nums)]
    winning_nums = [match.group() for match in re.finditer(pattern, winning_nums)]

    count_wins = sum(num in winning_nums for num in my_nums)
    return count_wins

def count_points(n_wins):
    """Counts the number fo points associated with the winning numbers

    Args:
        n_wins (int): number fo wins

    Returns:
        int: points collected
    """
    if n_wins == 0:
        return 0
    else:
        return 2 ** (n_wins - 1)

# First problem
counter = 0
for line in list_lines:
    counter += count_points(count_winning_numbers(line))
print(counter)

# Second problem
n_scratchcards = [1 for i in range(len(list_lines))]
for i, line in enumerate(list_lines):
    for j in range(count_winning_numbers(line)):
        # Add a number of following scratchcards equivalent 
        # to the current number of scratchcards
        n_scratchcards[min(i+j+1, len(list_lines))] += n_scratchcards[i] 
print(sum(n_scratchcards))