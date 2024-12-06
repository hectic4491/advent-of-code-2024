# pylint: skip-file
import numpy as np
import re


"""Problem 4; part 1"""
# I decided to practice my array shape manipulation skills while
# keeping some matrix properties in mind. Hence this approach is very
# "geometric". I transpose and shift the matrix in desired forms
# so that I can keep using the "cross_check" function. This required
# writing a few sub-functions.

DATA = []

try:
  with open("problem_4/input.txt", "r", encoding="UTF8") as f:
    for line in f:
      line = line.strip()
      DATA.append(line)
except FileNotFoundError as e:
  print(f"Error: {e}\nUsing the relative file path instead.\n")
  with open("input.txt", "r", encoding="UTF8") as f:
    for line in f:
      line = line.strip()
      DATA.append(line)


def data_itemized_list(data):
  itemized_list = []
  for string in data:
    itemized_list.append([char for char in string])
  return itemized_list


def offset_list(list, direction="right"):
  offset = []
  if direction == "right":
    for i in range(len(list)):
      head = ["." for _ in range(i)]
      tail = ["." for _ in range((len(list) - 1 - i))]

      sub_list = head + list[i] + tail
      offset.append(sub_list)

  elif direction == "left":
    for i in range(len(list)):
      head = ["." for _ in range((len(list) - 1 - i))]
      tail = ["." for _ in range(i)]

      sub_list = head + list[i] + tail
      offset.append(sub_list)
  return offset


def list_to_array(list):
  array = np.array(list)
  return array


def transpose_array(array):
  return np.transpose(array)


def array_to_list(array):
  return array.tolist()


def list_to_data(list):
  new_data = []
  for sublist in list:
    new_data.append(''.join(sublist))
  return new_data


def cross_check(data, pattern):
  count = 0
  for line in data:
    matches = re.findall(pattern, line)
    count += len(matches)
  return count


## Main ##
pattern = r"(?=(XMAS|SAMX))"


# Count the Horizontals:
horizontals = cross_check(DATA, pattern)
print(f"Horizontals: {horizontals}")


# Count the Verticals:
list = data_itemized_list(DATA)
array = list_to_array(list)
transposed = transpose_array(array)
list = array_to_list(transposed)
data = list_to_data(list)
verticals = cross_check(data, pattern)

print(f"Verticals: {verticals}")


# Count right diagnols
list = data_itemized_list(DATA)
offset = offset_list(list, "right")
array = list_to_array(offset)
transposed = transpose_array(array)
list = array_to_list(transposed)
data = list_to_data(list)
right_diagnols = cross_check(data, pattern)

print(f"Right diagnols: {right_diagnols}")


# Count left diagnols
list = data_itemized_list(DATA)
offset = offset_list(list, "left")
array = list_to_array(offset)
transposed = transpose_array(array)
list = array_to_list(transposed)
data = list_to_data(list)
left_diagnols = cross_check(data, pattern)

print(f"Left diagnols: {left_diagnols}")


solution = horizontals + verticals + right_diagnols + left_diagnols
print(f"Part 1 Solution: {solution}")


"""Problem 4; part 2"""


# Let's try a direct array access approach
def count_mas (data):
  count = 0
  for j in range(1, len(data) - 1):
    for i in range(1, len(data[j]) - 1):
      if data[j][i] == "A":
        if (((data[j-1][i-1] == "M" and data[j+1][i+1] == "S") or (
          data[j-1][i-1] == "S" and data[j+1][i+1] == "M")) and (
            (data[j-1][i+1] == "M" and data[j+1][i-1] == "S") or (
              data[j-1][i+1] == "S" and data[j+1][i-1] == "M"
              )
            )
          ):
          count += 1
  return count

print(f"Part 2 Solution: {count_mas(DATA)}")
