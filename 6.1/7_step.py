s = str(input())
if len(s) < 4:
    print('Длина строки меньше 4')
    
print(s[1] * 4)
print(s[-2:] + "!")
print(s[0:-3])
even_chars = s[::2]
odd_chars = s[1::2]
print(s + s.lower()[::-1])
print(odd_chars)
print(even_chars)