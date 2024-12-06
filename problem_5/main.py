# pylint: skip-file

"""Problem 5; part 1"""

RULES = []
UPDATES = []

with open("problem_5/input.txt", "r", encoding="utf8") as f:
  for line in f:
    if "|" in line:
      line = line.strip()
      rules = [int(page_number) for page_number in line.split('|')]
      RULES.append(rules)
    elif "," in line:
      line = line.strip()
      update = [int(page_number) for page_number in line.split(",")]
      UPDATES.append(update)

"""
Concept

Create a set of all unqiue pages.
Make a dictionary whose keys are the unique pages.
The value of the key:value pair will be another dictionary.
This inner dictionary will store Left and Right keys, where the value is
a list of numbers that must appear to the left or right of the outer
dictonary key.

Walk through each update. For each page in each update, we check if the
other pages are in the correct order.

If the set of pages to the right ever intersect the current page's left
set, we break. Vice Versa If the set of pages to the left ever
intersect the current page's right set, we break.

The validated sets have their middle value added to the sum.


Note** It's technically redundant to calculate both the "Left" and
"Right" sets of each key. It's sufficient to only calculate one,
and to only use that single comparison while walking through the update.
I.e. We would only need to calculate the intersection of each pages
'Left" set with the remaining right-sided relative pages to give us a
solution. Hence we could drop the 'Right' set and forgo making the second
'if' check with regards to the 'Right dictionary.

For now I'll leave them in so we can have a full picture of the approach.
"""

solution = 0

unique_pages = set([page for rule in RULES for page in rule])

rule_dict = {page: {'Left': set(), 'Right': set()} for page in unique_pages}

for rule in RULES:
  rule_dict[rule[0]]['Right'].add(rule[1])
  rule_dict[rule[1]]['Left'].add(rule[0])

for update in UPDATES:
  correct = True
  for i, page in enumerate(update):
    if set(update[i+1:]).intersection(rule_dict[page]['Left']):
      correct = False
      break
    if set(update[:i]).intersection(rule_dict[page]['Right']):
      correct = False
      break
  if correct:
    solution += update[len(update)//2]

print(f"Part 1 solution: {solution}")


"""Problem 5; part 2"""


