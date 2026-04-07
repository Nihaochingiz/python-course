# Получаем число в 6-чной системе счисления
num_base6 = input()

# Переводим из 6-чной в десятичную систему
decimal_number = int(num_base6, 6)

# Переводим из десятичной в 16-чную систему с префиксом '0x'
hexadecimal_number = hex(decimal_number)

# Выводим результат (с префиксом 0x)
print(hexadecimal_number)