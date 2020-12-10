from collections import Counter


with open('02-input.txt') as f:
  lines = [line.strip() for line in f.readlines()]
valid_count = 0
invalid_count = 0

for line in lines:
  split_line = line.split()
  min_val = int(split_line[0].split('-')[0])
  max_val = int(split_line[0].split('-')[1])
  character = split_line[1][0]
  password = split_line[2]
  password_counter = Counter(password)
  if min_val <= password_counter.get(character, 0) <= max_val:
    valid_count += 1
  else:
    invalid_count += 1
print(valid_count)

valid_count = 0
invalid_count = 0

for line in lines:
  split_line = line.split()
  first_index = int(split_line[0].split('-')[0]) - 1
  second_index = int(split_line[0].split('-')[1]) - 1
  character = split_line[1][0]
  password = split_line[2]
  if sum([password[first_index] == character, password[second_index] == character]) == 1:
    valid_count += 1
  else:
    invalid_count += 1
print(valid_count)

