a = int(input())
b = int(input())
n = int(input())

total_seconds = (a * 60 + b) * n

hours = total_seconds // 3600
minutes  = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(hours, minutes, seconds)