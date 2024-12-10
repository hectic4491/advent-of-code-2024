# pylint: skip-file

"""Problem 10; part 1"""

MATRIX = []
trailheads = set()
with open("problem_10/input.txt", "r", encoding="utf8") as f:
  j = 0
  for line in f:
    line = line.strip()
    MATRIX.append([int(n) for n in line])
    for i, n in enumerate(line):
      if n == '0':
        trailheads.add((j, i))
    j += 1


print(f"Matrix: {MATRIX}")
print(f"trailhads: {trailheads}")


# For each trailhead, It's 'score' is how many 9s it can reach.
# Calculate the sum of all scores.

