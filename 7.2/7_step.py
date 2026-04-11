# Считываем три строки ввода
required = set(input().split())
optional = set(input().split())
user_data = set(input().split())

# Проверяем условия:
# 1. Все обязательные строки присутствуют (required <= user_data)
# 2. Все строки пользователя либо обязательные, либо опциональные (user_data <= required | optional)

if required.issubset(user_data) and user_data.issubset(required | optional):
    print(True)
else:
    print(False)