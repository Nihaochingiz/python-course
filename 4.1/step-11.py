n1, n2, n3, n4 = [int(i) for i in input().split('.')]
# ваш код ниже (используйте переменные n1-n4)

result = (0 <= n1 <= 255 and 0 <= n2 <= 255 and 0 <= n3 <= 255 and 0 <= n4 <= 255) and not (n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0) and not (n1 == 255 and n2 == 255 and n3 == 255 and n4 == 255)

print(result)