# pylint: skip-file
""" Problem 3; part 1"""

# Import the RegEx library
import re

# Read File
TEXT_DATA = str()
with open("problem_3/input.txt", "r", encoding="UTF8") as f:
  for line in f:
    TEXT_DATA += line


# This pattern will find all necessary text strings.
PATTERN_1 = r"mul\(\d{1,3},\d{1,3}\)"


# Remove the excess characters on each string match
# until we just have subarrays of 2 ints.
INT_DATA_1 = []
matches_1 = re.findall(PATTERN_1, TEXT_DATA)
for string in matches_1:
  string = string.replace("mul(", "")
  string = string.replace(")", "")
  array = string.split(",")
  array[0] = int(array[0])
  array[1] = int(array[1])
  INT_DATA_1.append(array)


# Multiply the 2 ints in each subarray and add them to SOLUTION_1
SOLUTION_1 = 0
for subarray in INT_DATA_1:
  SOLUTION_1 += subarray[0] * subarray[1]


print(f"This is the solution to part 1: {SOLUTION_1}")


""" Problem 3; part 2"""


# This pattern will find all necessary text strings.
PATTERN_2 = r"do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)"
matches_2 = re.findall(PATTERN_2, TEXT_DATA)


# Now we build an array of accepted data using a running condition check.
ACCEPTED_DATA = []
accept = True

for string in matches_2:

  if string == "do()":
    accept = True
    continue

  if string == "don't()":
    accept = False
    continue

  if accept:
    ACCEPTED_DATA.append(string)


# Remove the excess characters on each string match
# until we just have subarrays of 2 ints.
INT_DATA_2 = []
for string in ACCEPTED_DATA:
  string = string.replace("mul(", "")
  string = string.replace(")", "")
  array = string.split(",")
  array[0] = int(array[0])
  array[1] = int(array[1])
  INT_DATA_2.append(array)


# Multiply the 2 ints in each subarray and add them to SOLUTION_2
SOLUTION_2 = 0
for subarray in INT_DATA_2:
  SOLUTION_2 += subarray[0] * subarray[1]


print(f"This is the solution to part 2: {SOLUTION_2}")