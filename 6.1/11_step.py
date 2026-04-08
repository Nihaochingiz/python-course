s = str(input())

if len(s) == 0:
    res = ''
    acc = 0
else:
    max_char = s[0]
    max_len = 1
    curr_char = s[0]
    curr_len = 1
    
    for i in range(1, len(s)):
        if s[i] == curr_char:
            curr_len += 1
        else:
            # Проверяем, нужно ли обновить максимум
            if curr_len >= max_len:  # >= для выбора последней при равенстве
                max_len = curr_len
                max_char = curr_char
            # Начинаем новую последовательность
            curr_char = s[i]
            curr_len = 1
    
    # Проверяем последнюю последовательность
    if curr_len >= max_len:
        max_len = curr_len
        max_char = curr_char
    
    res = max_char
    acc = max_len

print(res)
print(acc)