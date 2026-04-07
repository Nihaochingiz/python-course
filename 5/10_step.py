rows = int(input())
for i in range(rows, 0, -1):
    for j in range(rows, rows - i, -1):
        print(j, end=' ')
    print()