numbers = list(map(int, input().split()))
# Сортируем список
numbers.sort()

n = len(numbers)

# Находим медиану
if n % 2 == 1:
    median = numbers[n // 2]
    print(median) # для нечётной длины сразу выводим целое число
else:
    median = (numbers[n // 2 - 1] + numbers[ n//2]) / 2
    # Вывод с округлением для чётной длины
    if median.is_integer():
        print(int(median))
    else:
        print(round(median,1))