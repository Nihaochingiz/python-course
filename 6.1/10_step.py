s = str(input())
step = int(input())

res = ""
for char in s:
    new_char = chr((ord(char) - ord('a') - step) % 26 + ord('a'))
    res += new_char

print(res)