import re
import math

# Opens the data file and extracts the string as list of lines
f = open("input.txt", "r")
data = f.read()
list_lines = data.split('\n')

pattern = r'\d+'
races_times = [int(match.group()) for match in re.finditer(pattern, list_lines[0])]
races_records = [int(match.group()) for match in re.finditer(pattern, list_lines[1])]

def find_number_winning_possibilities(time_total, record):
    record_low_beaten, record_high_beaten = -1, -1
    time = 0
    while record_low_beaten == -1 and time <= time_total:
        distance = time * (time_total - time)
        if distance > record:
            record_low_beaten = time
        time += 1
    time = time_total
    while record_high_beaten == -1 and time >= 0:
        distance = time * (time_total - time)
        if distance > record:
            record_high_beaten = time
        time -= 1
    if record_high_beaten == -1 or record_low_beaten == -1:
        return 0
    return record_high_beaten - record_low_beaten + 1


total_possibilities = 1
for i, time in enumerate(races_times):
    n_possibilities = find_number_winning_possibilities(time, races_records[i])
    total_possibilities = total_possibilities * n_possibilities

print(total_possibilities)

# Harder example
long_time, long_record = int(''.join(map(str, races_times))), int(''.join(map(str, races_records)))
hard_possibilities = find_number_winning_possibilities(long_time, long_record)
print(hard_possibilities)