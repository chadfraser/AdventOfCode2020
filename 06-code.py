declarations = []
current_declaration = set()
with open('06-input.txt') as f:
  for line in f.readlines():
    if not line.strip():
      declarations.append(current_declaration)
      current_declaration = set()
    else:
      for char in line.strip():
        current_declaration.add(char)
  if current_declaration:
    declarations.append(current_declaration)
print(sum([len(x) for x in declarations]))

declarations = []
current_declaration = None
with open('06-input.txt') as f:
  for line in f.readlines():
    if not line.strip():
      declarations.append(current_declaration or set())
      current_declaration = None
    elif current_declaration is None:
      current_declaration = set()
      for char in line.strip():
        current_declaration.add(char)
    else:
      updated_declaration = set()
      for char in current_declaration:
        if char in line.strip():
          updated_declaration.add(char)
      current_declaration = updated_declaration
  if current_declaration:
    declarations.append(current_declaration)
print(sum([len(x) for x in declarations]))