# pylint: skip-file


"""Problem 6; part 1"""


class Guard ():
  def __init__(self):
    self.MAP = [] # define after opening file
    self.distinct_tiles = set() # define after opening file
    self.current_index = set() # define after opening file
    self.edge = False # assume we don't start at the edge
    self.facing = "North" # assume we start facing north
    self.direction = {"North": {"Turn": "East", "Delta_J": -1, "Delta_I": 0},
                  "East": {"Turn": "South", "Delta_J": 0, "Delta_I": 1},
                  "South": {"Turn": "West", "Delta_J": 1, "Delta_I": 0},
                  "West": {"Turn": "North", "Delta_J": 0, "Delta_I": -1}}

    # initialize MAP, distinct_tiles, current_index.
    with open("problem_6/input.txt", "r", encoding="utf8") as f:
      j = 0
      for line in f:
        line = line.strip()
        i = line.find("^")
        if i != -1:
          self.current_index = (j, i)
          self.distinct_tiles.add(self.current_index)
        array = [char for char in line]
        self.MAP.append(array)
        j += 1


  def look_ahead(self):
    j, i = self.current_index

    j_max = len(self.MAP)
    i_max = len(self.MAP[0])

    if j == 0 or j == j_max or i == 0 or i == i_max:
      print(f"Looking at edge")
      return "Edge"

    else:
      j += self.direction[self.facing]["Delta_J"]
      i += self.direction[self.facing]["Delta_I"]
      print(f"Looking at: ({j}, {i}) -> {self.MAP[j][i]}")
      return self.MAP[j][i]


  def turn(self):
    print(f"Turning from {self.facing} to {self.direction[self.facing]['Turn']}")
    self.facing = self.direction[self.facing]["Turn"]


  def move(self):
    delta_j = self.direction[self.facing]['Delta_J']
    delta_i = self.direction[self.facing]['Delta_I']

    j, i = self.current_index

    print(f"Moving from ({j}, {i}) to ({j + delta_j}, {i + delta_i})")

    self.current_index = (j + delta_j, i + delta_i)
    self.distinct_tiles.add(self.current_index)


  def patrol(self):
    while not self.edge:
      next_tile = self.look_ahead()
      if next_tile == "Edge":
        self.edge = True
        continue
      elif next_tile == "#":
        self.turn()
        continue
      self.move()


guard = Guard()
guard.patrol()
print(f"The guard will patrol {len(guard.distinct_tiles)} unique tiles.")


"""Problem 6; part 2"""
