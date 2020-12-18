import json

with open('json_example_QAP.json', encoding='utf8') as file:  # Открываем файл
    strfile = file.read()
    templates_resp = json.loads(strfile)



# Список полей в шаблоне
fields_list = ['timestamp',
                    'referer',
                    'location',
                    'remoteHost',
                    'partyId',
                    'sessionId',
                    'pageViewId',
                    'eventType',
                    'item_id',
                    'item_price',
                    'item_url',
                    'basket_price',
                    'detectedDuplicate',
                    'detectedCorruption',
                    'firstInSession',
                    'userAgentName']


m = 1  # Создаем счетчик тестов
file_03 = open('output_tests.txt', 'w', encoding='UTF8')  # запись результатов в новый файл

for templates in templates_resp:
    k = 0  # Создаем счетчик ошибок в тестах
    file_03.write(f'\nТест {m}\n')
    for field in templates:  # определяем лишние поля в ответе
        extra_fields = []
        if field not in fields_list:
            extra_fields.append(field)
            extra_fields = (', '.join(extra_fields))
            file_03.write(f'False - В ответе присутствует лишнее поле - {extra_fields}\n')
            k = k + 1

    try:
        if 'timestamp' not in templates:  # опредеяем отсутствующие поля в ответе
            file_03.write(f'False - В ответе отсутствует поле - timestamp\n')
            k = k + 1
    except:
        None

    if 'timestamp' in templates and type(
            templates['timestamp']) != int:  # опредеяем соответствие ответа заданным условиям
        file_03.write(f'False - Поле timestamp не является int\n')
        k = k + 1

    try:
        if 'referer' not in templates:
            file_03.write(f'False - Поле referer отсутствует\n')
            k = k + 1
    except:
        None

    if 'referer' in templates and type(templates['referer']) != str:
        file_03.write(f'False - Поле referer не является string\n')
        k = k + 1

    try:
        if 'referer' in templates and not (
                templates['referer'].startswith('https://') or templates['referer'].startswith('http://')):
            file_03.write(f'False - Поле referer не является url\n')
            k = k + 1
    except:
        None

    try:
        if 'location' not in templates:
            file_03.write(f'False - Поле location отсутствует\n')
            k = k + 1
    except:
        None

    if 'location' in templates and type(templates['location']) != str:
        file_03.write(f'False - Поле location не является string\n')
        k = k + 1
    try:
        if 'location' in templates and not (
                templates['location'].startswith('https://') or templates['location'].startswith('http://')):
            file_03.write(f'False - Поле location не является url\n')
            k = k + 1
    except:
        None

    try:
        if 'remoteHost' not in templates:
            file_03.write(f'False - Поле remoteHost отсутствует\n')
            k = k + 1
    except:
        None

    if 'remoteHost' in templates and type(templates['remoteHost']) != str:
        file_03.write(f'False - Поле remoteHost не является string\n')
        k = k + 1

    try:
        if 'partyId' not in templates:
            file_03.write(f'False - Поле partyId отсутствует\n')
            k = k + 1
    except:
        None

    if 'partyId' in templates and type(templates['partyId']) != str:
        file_03.write(f'False - Поле partyId не является string\n')
        k = k + 1

    try:
        if 'sessionId' not in templates:
            file_03.write(f'False - Поле sessionId отсутствует\n')
            k = k + 1
    except:
        None

    if 'sessionId' in templates and type(templates['sessionId']) != str:
        file_03.write(f'False - Поле sessionId не является string\n')
        k = k + 1

    try:
        if 'pageViewId' not in templates:
            file_03.write(f'False - Поле pageViewId отсутствует\n')
            k = k + 1
    except:
        None

    if 'pageViewId' in templates and type(templates['pageViewId']) != str:
        file_03.write(f'False - Поле pageViewId не является string\n')
        k = k + 1

    try:
        if 'eventType' not in templates:
            file_03.write(f'False - Поле eventType отсутствует\n')
            k = k + 1
    except:
        None

    if 'eventType' in templates and type(templates['eventType']) != str:
        file_03.write(f'False - Поле eventType не является string\n')
        k = k + 1

    try:
        if 'eventType' in templates and (
                (templates['eventType']) != 'itemBuyEvent' and (templates['eventType']) != 'itemViewEvent'):
            file_03.write(f'False - Поле eventType не является itemBuyEvent или itemViewEvent\n')
            k = k + 1
    except:
        None

    try:
        if 'item_id' not in templates:
            file_03.write(f'False - Поле item_id отсутствует\n')
            k = k + 1
    except:
        None

    if 'item_id' in templates and type(templates['item_id']) != str:
        file_03.write(f'False - Поле item_id не является string\n')
        k = k + 1

    try:
        if 'item_price' not in templates:
            file_03.write(f'False - Поле item_price отсутствует\n')
            k = k + 1
    except:
        None

    if 'item_price' in templates and type(templates['item_price']) != int:
        file_03.write(f'False - Поле item_price не является int\n')
        k = k + 1

    try:
        if 'item_url' not in templates:
            file_03.write(f'False - Поле item_url отсутствует\n')
            k = k + 1
    except:
        None

    if 'item_url' in templates and type(templates['item_url']) != str:
        file_03.write(f'False - Поле item_url не является string\n')
        k = k + 1

    try:
        if 'item_url' in templates and not (
                templates['item_url'].startswith('https://') or templates['location'].startswith('http://')):
            file_03.write(f'False - Поле item_url не является url\n')
            k = k + 1
    except:
        None

    try:
        if 'basket_price' not in templates:
            file_03.write(f'False - Поле basket_price отсутствует\n')
            k = k + 1
    except:
        None

    if 'basket_price' in templates and type(templates['basket_price']) != str:
        file_03.write(f'False - Поле basket_price не является string\n')
        k = k + 1

    try:
        if 'detectedDuplicate' not in templates:
            file_03.write(f'False - Поле detectedDuplicate отсутствует\n')
            k = k + 1
    except:
        None

    if 'detectedDuplicate' in templates and type(templates['detectedDuplicate']) != bool:
        file_03.write(f'False - Поле detectedDuplicate не является bool\n')
        k = k + 1

    try:
        if 'detectedCorruption' not in templates:
            file_03.write(f'False - Поле detectedCorruption отсутствует\n')
            k = k + 1
    except:
        None

    if 'detectedCorruption' in templates and type(templates['detectedCorruption']) != bool:
        file_03.write(f'False - Поле detectedCorruption не является bool\n')
        k = k + 1

    try:
        if 'firstInSession' not in templates:
            file_03.write(f'False - Поле firstInSession отсутствует\n')
            k = k + 1
    except:
        None

    if 'firstInSession' in templates and type(templates['firstInSession']) != bool:
        file_03.write(f'False - Поле firstInSession не является bool\n')
        k = k + 1

    try:
        if 'userAgentName' not in templates:
            file_03.write(f'False - Поле userAgentName отсутствует\n')
            k = k + 1
    except:
        None

    if 'userAgentName' not in templates and type(templates['userAgentName']) != str:
        file_03.write(f'False - Поле userAgentName не является string\n')
        k = k + 1

    if k != 0:  # подсчитываем количество ошибок
        file_03.write(f'Найдено {k} ошибок\n')

    else:
        file_03.write('PASS - Тест пройден!\n')

    m = m + 1


file_03.close()  # закрытие файла
