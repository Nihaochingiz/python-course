a = {int(i) for i in input().split()}
# Сумма квадратов чисел в множестве
res = 0
for num in a:
    res += num ** 2
    
print(res)



