with open('05-input.txt') as f:
  seats = [line.strip() for line in f.readlines()]
highest_seat_id = 0
seat_ids = set()
for seat in seats:
  row = 0
  col = 0
  for idx, char in enumerate(seat[:7]):
    if char == 'B':
      row += 64 // (2 ** idx)
  for idx, char in enumerate(seat[7:]):
    if char == 'R':
      col += 4 // (2 ** idx)
  seat_id = row * 8 + col
  seat_ids.add(seat_id)
  if seat_id > highest_seat_id:
    highest_seat_id = seat_id
print(highest_seat_id)

for seat_id in seat_ids:
  if seat_id + 1 not in seat_ids and seat_id + 2 in seat_ids:
    print(seat_id + 1)
