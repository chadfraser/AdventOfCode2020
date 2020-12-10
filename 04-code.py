import re


required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def is_valid(passport):
  for key in required_keys:
    if key not in passport:
      return False
  return True

def is_fully_valid(passport):
  return all([is_valid(passport) and validate_byr(passport) and validate_iyr(passport) and validate_eyr(passport) and
              validate_hgt(passport) and validate_hcl(passport) and validate_ecl(passport) and validate_pid(passport)])

def validate_byr(passport):
  byr_regex = re.compile('\d{4}$')
  return byr_regex.match(passport['byr']) and 1920 <= int(passport['byr']) <= 2002

def validate_iyr(passport):
  iyr_regex = re.compile('\d{4}$')
  return iyr_regex.match(passport['iyr']) and 2010 <= int(passport['iyr']) <= 2020

def validate_eyr(passport):
  eyr_regex = re.compile('\d{4}$')
  return eyr_regex.match(passport['eyr']) and 2020 <= int(passport['eyr']) <= 2030

def validate_hgt(passport):
  hgt_regex = re.compile('(\d{2,3})(cm|in)$')
  hgt_match = hgt_regex.match(passport['hgt'])
  return hgt_match and ((hgt_match.group(2) == 'cm' and 150 <= int(hgt_match.group(1)) <= 193) or
      (hgt_match.group(2) == 'in' and 59 <= int(hgt_match.group(1)) <= 76))

def validate_hcl(passport):
  hcl_regex = re.compile('#[0-9a-f]{6}$')
  return hcl_regex.match(passport['hcl'])

def validate_ecl(passport):
  ecl_regex = re.compile('(amb|blu|brn|gry|grn|hzl|oth)$')
  return ecl_regex.match(passport['ecl'])

def validate_pid(passport):
  pid_regex = re.compile('\d{9}$')
  return pid_regex.match(passport['pid'])

with open('04-input.txt') as f:
  passports = []
  current_passport = {}
  for line in f.readlines():
    if not line.strip():
      passports.append(current_passport)
      current_passport = {}
    else:
      key_value_pairs = line.split()
      for pair in key_value_pairs:
        key, value = pair.split(":")
        current_passport[key] = value
  if current_passport:
    passports.append(current_passport)
total_valid_passports = 0
for passport in passports:
  if is_valid(passport):
    total_valid_passports += 1
print(total_valid_passports)

total_fully_valid_passports = 0
for passport in passports:
  if is_fully_valid(passport):
    total_fully_valid_passports += 1
print(total_fully_valid_passports)
