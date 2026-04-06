from decimal import Decimal, getcontext

# Устанавливаем точность 60 знаков
getcontext().prec = 60

# Ввод чисел
a = Decimal(input())
b = Decimal(input())

# Вычисляем квадратный корень из a и прибавляем b
result = a.sqrt() + b

# Выводим результат
print(result)