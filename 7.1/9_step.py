numbers = list(map(int, input().split()))

max_num = max(numbers)

second_max = max(num for num in numbers if num != max_num)

print(second_max)
