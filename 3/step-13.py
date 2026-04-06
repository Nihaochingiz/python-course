apartment_cost = int(input()) # стоимость квартиры
annual_percentage = int(input()) # процент годовых
initial_payment = int(input()) # первоначальный взнос
annual_payment = int(input()) # ежегодная выплата

credit = apartment_cost - initial_payment

# расчет по годам
for year in range(1,4): # 3 года
    # Сначала вычитаем выплату, потом начисляем проценты
    credit = (credit - annual_payment) * (1 + annual_percentage / 100)
    # Отбрасываем дробную часть
    credit = int(credit)
    # Выводим остаток долга
    print(credit)
