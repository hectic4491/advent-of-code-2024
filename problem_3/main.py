import re

DATA = []
with open("problem_3/input.txt", "r", encoding="UTF8") as f:
    for report in f:
        DATA.append([int(n) for n in report.split()])


# This pattern will find all necessary text strings
pattern = r"mul\(\d{1,3},\d{1,3}\)" 

pattern = re.findall(pattern, DATA)

print(pattern)
