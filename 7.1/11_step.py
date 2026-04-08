numbers = list(map(int, input().split()))

even_numbers = [x for x in numbers if x % 2 == 0]
print(*even_numbers)