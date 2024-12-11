# pylint: skip-file


""" This is a math problem... """


"""

1.
If the stone is engraved with the number 0, it is replaced by a stone
engraved with the number 1.

  i.e. Find the single stone zeros and replace them with 1
2.
If the stone is engraved with a number that has an even number of digits,
it is replaced by two stones. The left half of the digits are engraved 
on the new left stone, and the right half of the digits are engraved
on the new righth stone. (The new numbers don't keep extra leading zeros:
1000 would become stone 10 and 0.)

  i.e. We only have to do the zero check on the right stone because the left
       stone couldn't have leading zeros by definition.

3.
If none of the other rules apply, the stone is replaced by a new stone;
the old stone's number multiplied by 2024 is engraved on the new stone.

  i.e. We have to keep track of which stones have already been changed before
       we can decide which ones to apply this rule two.
       By definition, all even number digit stones can't have the third rule 
       applied, because they would have been changed by the second rule. But not
       all odd number digit stones will be changed by this rule.

       Potential solution: have a companion data object that stores which of the
       arrangements index accesses is valid for rule_three. This object need only
       be a list of numbers.
       

**
No matter how the stones change, their order is preserved, and they stay
on their perfectly straight line.

**
The stones each simultaneously change according to the first applicable
rule in the list.


How many stones will you have after blinking 25 times?


// first state
: 6563348 67 395 0 6 4425 89567 739318
                 ^
                 rule 1

// second state


// third state



"""

with open("problem_11/input.txt", "r", encoding="utf8") as f:
  for line in f:
    line = line.strip()
    DATA = [line for line in line.split()]  # treat them as strings


def rule_one(arrangement):
  unchanged = [i for i in range(len(arrangement))]

  for i, stone in enumerate(arrangement):
    if '0' in stone and len(stone) == 1:
      arrangement[i] = '1'
      unchanged.pop(i)
  
  return arrangement, unchanged
      

def rule_two(arrangement, unchaged):
  """
  new_stone is the new 'right' stone placed at arrangement[i]. Do it 
  after the for loop ends.

  The stone accessed during the for loop will become the 'left' stone.
  """
  new_stones = {}
  for i, stone in enumerate(arrangement):
    if len(stone) % 2 == 0:
      new_stone = int(stone[len(stone)//2:])    
      new_stones[i + len(new_stones) + 1] = str(new_stone)
      arrangement[i] = stone[:len(stone)//2]
      print(unchanged) ### TODO ### <- updated the changed indicies in this function
  for key in new_stones:
    arrangement.insert(key, new_stones[key])



# print(DATA)
# rule_one(DATA)
# print(DATA)
# rule_two(DATA)
# print(DATA)

myList = ['1000', '0', '1425', '234']

print(myList)
myList, unchanged = rule_one(myList)
print(myList)
print(unchanged)
rule_two(myList)
print(myList)
