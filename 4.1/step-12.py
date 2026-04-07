s1 = input()
s2 = input()
s3 = input()

a = len(s1)
b = len(s2)
c = len(s3)

min_len = min(a, b, c)

if c == min_len:
    print(s3)
elif b == min_len:
    print(s2)
else: 
    print(s1)