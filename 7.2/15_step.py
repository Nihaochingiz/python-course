def count_request_server():
    # создаем два словаря (dict)
    url_counter = {}
    status_counter = {}

    # ждем ввод с клавиатуры
    # строку разделяем по пробелы
    # если пишем end то прекращаем ввод
    while True:
        line = input().strip()
        if line == 'end':
            break

        # разделяем строку на адрес и код статуса
        parts = line.split()
        if len(parts) != 2:
            continue  # пропускаем некорректные строки
        # распаковываем список parts на две переменные url и status
        url, status = parts

        # подсчет по адресам
        if url not in url_counter:
            # обращаемся к элементу словаря по ключевому слову url
            url_counter[url] = 0
        url_counter[url] += 1

        # подсчет по статус-кодам
        if status not in status_counter:
            # обращаемся к элементу словаря по ключевому слову status
            status_counter[status] = 0
        status_counter[status] += 1

    # сортировка по возрастанию
    for status in sorted(status_counter.keys()):
        print(f"{status} {status_counter[status]}")

    # сортировка по алфавиту
    for url in sorted(url_counter.keys()):
        print(f"{url} {url_counter[url]}")

count_request_server()