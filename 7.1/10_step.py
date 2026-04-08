numbers = list(map(int, input().split()))
new_numbers = []

for num in numbers:
    if num != 0:
        new_numbers.append(num)

for num in numbers:
    if num == 0:
        new_numbers.append(num)

print(' '.join(map(str, new_numbers)))