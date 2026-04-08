numbers = list(map(int, input().split()))
product = 1
for num in numbers:
    product *=num
    
print(product)