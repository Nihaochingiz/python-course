import json


def find_max_age(obj, current_max=0):
    """
    Рекурсивно находит максимальное значение возраста (age) во вложенных структурах данных.

    Args:
        obj: Объект для анализа (может быть dict, list или другой тип)
        current_max: Текущее найденное максимальное значение (по умолчанию 0)

    Returns:
        Максимальное значение возраста среди всех найденных полей 'age'
    """

    # запускаем проверку является ли объект словарем, если да
    if isinstance(obj, dict):
        # далее получаем через метод словаря items пары ключ-значения
        for key, value in obj.items():
            # если ключ age и значение является int или float
            if key == "age" and isinstance(value, (int, float)):
                # функция, которая возвращает наибольшее из двух значений current_max и value
                # обновляем текущий максимум, если нашли большее значение
                current_max = max(current_max, value)
            else:
                # рекурсивно обрабатываем значение по текущему ключу
                # передаём найденный максимум дальше в глубину структуры
                current_max = find_max_age(value, current_max)

    # проверяем, является ли объект списком
    elif isinstance(obj, list):
        # перебираем все элементы списка
        for item in obj:
            # рекурсивно обрабатываем каждый элемент списка
            # передаём текущий максимум для сохранения найденного значения
            current_max = find_max_age(item, current_max)

    # возвращаем максимальное найденное значение
    # для других типов данных (int, str, None и т.д.) просто возвращаем current_max без изменений
    return current_max

d = json.loads(input().strip())

res = find_max_age(d)

print(res)
