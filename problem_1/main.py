"""Problem 1; part 1"""

"""When we have strong ideas of the input, we can do
a direct method of testing to find a quick solution."""

left_array = []
right_array = []
differences = []

with open("problem_1/input.txt", "r") as f:
  for line in f:
    left, right = line.split()

    left_array.append(int(left))
    right_array.append(int(right))

left_array.sort()
right_array.sort()

for i in range(len(left_array)):
  differences.append(abs(left_array[i] - right_array[i]))

answer = sum(differences)

print(f"Problem 1.1 solution: {answer}")


"""Problem 1; part 2"""

right_occurrences = {}
similarity = []

for number in right_array:
  if number in right_occurrences:
    right_occurrences[number] += 1
  else:
    right_occurrences[number] = 1

for number in left_array:
  if number in right_occurrences:
    similarity.append(number * right_occurrences[number])

print(f"Problem 1.2 solution: {sum(similarity)}")
