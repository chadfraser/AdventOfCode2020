import math


def count_trees(map, horizontal_movement, vertical_movement):
  x_coord = 0
  y_coord = 0
  trees_hit = 0
  map_width = len(toboggan_map[0])
  map_height = len(toboggan_map)

  while True:
    x_coord += horizontal_movement
    x_coord %= map_width
    y_coord += vertical_movement
    if y_coord >= map_height:
      break
    if toboggan_map[y_coord][x_coord] == '#':
      trees_hit += 1
  return trees_hit

with open('03-input.txt') as f:
  toboggan_map = [[char for char in line.strip()] for line in f.readlines()]

trees_hit = count_trees(toboggan_map, 3, 1)
print(trees_hit)

trees_hit_amounts = []
for coords in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
  trees_hit_amounts.append(count_trees(toboggan_map, coords[0], coords[1]))
print(math.prod(trees_hit_amounts))