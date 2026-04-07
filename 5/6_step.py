a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i == a:
        print(i)
    else:
        if (i - a) % 2 == 1:
            print(-i)
        else:
            print(i)