# читаем входную строку
s = input().strip()

# разбиваем строку на слова
words = s.split()

# считаем частоту каждого слова
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1
    
# сортируем ключи в алфавитном порядке
sorted_keys = sorted(word_count.keys())

for key in sorted_keys:
    print(key, word_count[key])
