product = 1
has_numbers = False

while True:
    num = int(input())
    
    if num == 0:
        break
    
    product *= num
    has_numbers = True
    
if not has_numbers:
    product = 1
    
print(product)