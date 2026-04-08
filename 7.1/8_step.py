# Читаем числа
numbers = list(map(int, input().split()))

# Создаем список для сумм
sums = []

# Проходим по числам от 0 до предпоследнего индекса
for i in range(len(numbers) - 1):
    # Суммируем текущее и следующее число
    sums.append(numbers[i] + numbers[i + 1])

# Выводим суммы через пробел
print(' '.join(map(str, sums)))
    