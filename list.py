rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix = []

for r in range(rows):
    row_list = []
    print(f"\nRow {r+1}")
    for c in range(cols):
        num = float(input(f"Enter number{c+1}: "))
        row_list.append(num)
    matrix.append(row_list)

print("\nMatrix stored:")
for r in range(rows):
    print(f"Row {r+1}: {matrix[r]}")

search_num = float(input("\nSearch: "))

found = []
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == search_num:
            found.append((r+1, c+1))

if found:
    print("\nThe numbers are found at positions (row, col):")
    for pos in found:
        print(pos)
else:
    print("\nNumber not found.")
