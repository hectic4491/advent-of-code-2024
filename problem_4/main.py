# pylint: skip-file
from pprint import pprint
import numpy as np
import re


DATA = []
with open("problem_4/input.txt", "r", encoding="UTF8") as f:
  for line in f:
    line = line.strip()
    DATA.append(line)


def data_itemized_list(data):
  itemized_list = []
  for string in data:
    itemized_list.append([c for c in string])
  return itemized_list


def diagnolize_list(list, direction="right"):
  diagonal_list = []
  if direction == "right":
    for i in range(len(list)):
      head = ["." for _ in range(i)]
      tail = ["." for _ in range((len(list) - 1 - i))]

      sub_list = head + list[i] + tail
      diagonal_list.append(sub_list)

  elif direction == "left":
    for i in range(len(list)):
      head = ["." for _ in range((len(list) - 1 - i))]
      tail = ["." for _ in range(i)]

      sub_list = head + list[i] + tail
      diagonal_list.append(sub_list)


  return diagonal_list


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
diagnol = diagnolize_list(list, "right")
array = list_to_array(diagnol)
transposed = transpose_array(array)
list = array_to_list(transposed)
data = list_to_data(list)
right_diagnols = cross_check(data, pattern)

print(f"Right diagnols: {right_diagnols}")


# Count left diagnols
list = data_itemized_list(DATA)
diagnol = diagnolize_list(list, "left")
array = list_to_array(diagnol)
transposed = transpose_array(array)
list = array_to_list(transposed)
data = list_to_data(list)
left_diagnols = cross_check(data, pattern)

print(f"Left diagnols: {left_diagnols}")


solution = horizontals + verticals + right_diagnols + left_diagnols
print(f"Solution: {solution}")