import re


def change_instruction(instructions):
  for instruction in instructions:
    original_value = instruction[0]
    if original_value == 'acc':
      continue
    elif original_value == 'nop':
      instruction[0] = 'jmp'
    else:
      instruction[0] = 'nop'

    current_acc = 0
    current_instruction_index = 0
    visited_instructions = set()
    while True:
      visited_instructions.add(current_instruction_index)
      if current_instruction_index == len(instructions):
        print(current_acc)
        return
      [current_instruction, sign, value] = instructions[current_instruction_index]
      if current_instruction == 'nop':
        current_instruction_index += 1
      elif current_instruction == 'acc':
        if sign == '+':
          current_acc += int(value)
        else:
          current_acc -= int(value)
        current_instruction_index += 1
      elif current_instruction == 'jmp':
        if sign == '+':
          current_instruction_index += int(value)
        else:
          current_instruction_index -= int(value)
      if current_instruction_index in visited_instructions:
        break
    instruction[0] = original_value



instructions = []
instruction_regex = re.compile('(acc|jmp|nop) ([+-])(\d+)')
with open('08-input.txt') as f:
  for line in f.readlines():
    if line.strip():
      instruction_match = instruction_regex.match(line.strip())
      instructions.append([instruction_match.group(1), instruction_match.group(2), instruction_match.group(3)])

current_acc = 0
current_instruction_index = 0
visited_instructions = set()
while True:
  visited_instructions.add(current_instruction_index)
  [current_instruction, sign, value] = instructions[current_instruction_index]
  if current_instruction == 'nop':
    current_instruction_index += 1
  elif current_instruction == 'acc':
    if sign == '+':
      current_acc += int(value)
    else:
      current_acc -= int(value)
    current_instruction_index += 1
  elif current_instruction == 'jmp':
    if sign == '+':
      current_instruction_index += int(value)
    else:
      current_instruction_index -= int(value)
  if current_instruction_index in visited_instructions:
    print(current_acc)
    break

change_instruction(instructions)