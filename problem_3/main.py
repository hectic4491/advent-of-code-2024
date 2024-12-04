# pylint: skip-file
""" Problem 3; part 1"""

# Import the RegEx library
import re

# This pattern will find all necessary text strings.
PATTERN = r"mul\(\d{1,3},\d{1,3}\)"

TEXT_DATA = str()
with open("problem_3/input.txt", "r", encoding="UTF8") as f:
  for line in f:
    TEXT_DATA += line

# Remove the excess characters on each string match
# until we just have subarrays of 2 ints.
INT_DATA = []
matches = re.findall(PATTERN, TEXT_DATA)
for string in matches:
  string = string.replace("mul(", "")
  string = string.replace(")", "")
  array = string.split(",")
  array[0] = int(array[0])
  array[1] = int(array[1])
  INT_DATA.append(array)

# Multiply the 2 ints in each subarray and add them to SOLUTION_1
SOLUTION_1 = 0
for subarray in INT_DATA:
  SOLUTION_1 += subarray[0] * subarray[1]

print(f"This is the solution to part 1: {SOLUTION_1}")


""" Problem 3; part 2"""
