from collections import defaultdict
import re


reverse_bag_contents = defaultdict(list)
bag_contents = defaultdict(dict)
bag_regex = re.compile('(.*) bags contain (.*)$')
contents_regex = re.compile('(\d*) (.*) bag(s)?$')
with open('07-input.txt') as f:
  for line in f.readlines():
    if line.strip():
      bag_match = bag_regex.match(line.strip())
      contents = bag_match.group(2)
      if contents == 'no other bags.':
        continue
      else:
        contents_list = contents[:-1].split(", ")
        contents_match = [contents_regex.match(x).group(2) for x in contents_list]
        quantity_match = [contents_regex.match(x).group(1) for x in contents_list]
        for content, quantity in zip(contents_match, quantity_match):
          reverse_bag_contents[content].append(bag_match.group(1))
          bag_contents[bag_match.group(1)][content] = int(quantity)

bag_to_bring = 'shiny gold'
bags_to_contain = set()
bags_to_check = [bag_to_bring]
while bags_to_check:
  current_bag = bags_to_check.pop()
  for bag_color in reverse_bag_contents[current_bag]:
    bags_to_contain.add(bag_color)
    bags_to_check.append(bag_color)
print(len(bags_to_contain))

total_bag_count_required = 1
bags_to_calculate = list(reverse_bag_contents.keys())
bags_requirements_calculated = {}
while bags_to_calculate:
  current_bag = bags_to_calculate.pop(0)
  if not all(x in bags_requirements_calculated for x in bag_contents[current_bag]):
    bags_to_calculate.append(current_bag)
  else:
    current_bag_requirement = sum(bag_contents[current_bag][x] * (1 + bags_requirements_calculated[x]) for x in bag_contents[current_bag])
    bags_requirements_calculated[current_bag] = current_bag_requirement
print(bags_requirements_calculated[bag_to_bring])