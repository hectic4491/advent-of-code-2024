import re


PATTERN = r"mul\(\d{1,3},\d{1,3}\)"
DATA = str()

with open("problem_3/input.txt", "r", encoding="UTF8") as f:
    for line in f:
        DATA += line

# This pattern will find all necessary text strings

matches = re.findall(PATTERN, DATA)
print(matches)
