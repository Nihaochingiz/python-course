husband_income = float(input())
wife_income = float(input())

total_income = husband_income + wife_income

# Переводим в копейки для точных вычислений без проблем с плавающей точкой
total_kopecks = int(round(total_income * 100))

percentages = {
    "Отпуск": 10,
    "Пропитание и еда": 30,
    "Коммунальные платежи": 5,
    "Досуг": 15,
    "Накопления": 40
}

results = {}

# Считаем сумму для каждой категории кроме накоплений

total_allocated = 0

for category, percent in percentages.items():
    if category != "Накопления":
        # Считаем количество копеек для категории
        category_kopecks = total_kopecks * percent // 100
        results[category] = category_kopecks
        total_allocated += category_kopecks
        
# Накопления = остаток
results["Накопления"] = total_kopecks - total_allocated

# Вывод результатов
for category in ["Отпуск", "Пропитание и еда", "Коммунальные платежи", "Досуг", "Накопления"]:
    kopecks = results[category]
    rubles = kopecks // 100
    cents = kopecks % 100
    print(f"{category}: {rubles} руб. {cents} коп.")
        