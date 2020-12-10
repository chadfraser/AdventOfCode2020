def part_one(lines):
  for idx, line in enumerate(lines):
    for following_line in lines[idx+1:]:
      if int(line) + int(following_line) == 2020:
        return int(line) * int(following_line)


with open('01-input.txt') as f:
  lines = [line.strip() for line in f.readlines()]
print(part_one(lines))

for idx, line in enumerate(lines):
  for idx2, following_line in enumerate(lines[idx+1:]):
    for further_line in lines[idx2+1:]:
      if int(line) + int(following_line) + int(further_line) == 2020:
        print(int(line) * int(following_line) * int(further_line))