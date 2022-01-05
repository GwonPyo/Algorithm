location = input()
# col = location[0]
# row = int(location[1])

# if col >= 'c' and col <= 'f':
#     if row >= 3 and row <= 6:
#         print(8)
#     elif row == 2 or row == 7:
#         print(6)
#     elif row == 1 or row == 8:
#         print(4)

# elif col == 'h' or col == 'g':
#     if row >= 3 and row <= 6:
#         print(6)
#     elif row == 2 or row == 7:
#         print(4)
#     elif row == 1 or row == 8:
#         print(3)

# elif col == 'a' or col == 'h':
#     if row >= 3 and row <= 6:
#         print(4)
#     elif row == 2 or row == 7:
#         print(3)
#     elif row == 1 or row == 8:
#         print(2)

row = int(location[1])
column = int(ord(location[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

count = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1

print(count)