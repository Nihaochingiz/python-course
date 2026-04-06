import math

# Считываем размеры товара
width = float(input())
height = float(input())
depth = float(input())

# Округляем вверх до целого числа
box_width = math.ceil(width)
box_height = math.ceil(height)
box_depth = math.ceil(depth)

# Выводим размеры коробки
print(box_width)
print(box_height)
print(box_depth)