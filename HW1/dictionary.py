rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix = {}

for r in range(1, rows + 1):
    row_list = []
    print(f"\nRow {r}")
    for c in range(1, cols + 1):
        num = float(input(f"Enter number{c}: "))
        row_list.append(num)
    matrix[r] = row_list

print("\nMatrix stored:")
for r, values in matrix.items():
    print(f"Row {r}: {values}")

search_num = float(input("\nSearch: "))

found = []
for r, values in matrix.items():
    for c, val in enumerate(values, start=1):
        if val == search_num:
            found.append((r, c))

if found:
    print("\nThe numbers are found at positions (row, col):")
    for pos in found:
        print(pos)
else:
    print("\nNumber not found.")
