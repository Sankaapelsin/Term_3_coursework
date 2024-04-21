import json
import datetime


def loads():
    """Открываем файл с данными и читаем его"""
    with open("data/operations.json", "r", encoding='utf8') as file:
        operations = json.load(file)
        return operations


def executed_operations():
    """Функция для сортировки операций по исполнению,
     возвращает только выполненые операции"""
    data = loads()
    executed_op = []
    for operation in data:
        if operation != {}:
            if operation['state'] == 'EXECUTED':
                executed_op.append(operation)
        else:
            pass
    return executed_op


def five_last_operations():
    """Функция для сортировки операций, возвращает 5 последних операций"""
    data = executed_operations()
    sorted_list = sorted(data, key=lambda x: x['date'], reverse=True)
    five_sorted = sorted_list[:5]
    return five_sorted


def date_formatting():
    """Функция для форматирования даты и времени в привычный формат,
     возвращает данные об последних пяти операциях с отформатированной датой"""
    data = five_last_operations()
    for operation in data:
        date_time_str = operation['date']
        date_time_obj = datetime.datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%S.%f")
        new_date = date_time_obj.strftime("%Y.%m.%d")
        operation['date'] = new_date
    return data


def secure_for_card_number():
    """Функция для шифрования (скрытия) данных карты или счета,
      возвращает данные об последних пяти операциях
      с зашифрованныии данными и отформатированной датой"""
    data = date_formatting()
    for operation in data:
        if operation['description'] == 'Открытие вклада' or operation['description'] == 'Перевод организации':
            secure_count = 'Счет **' + operation['to'][-4:]
            operation['to'] = secure_count
        elif operation['description'] == 'Перевод организации':
            i = 0  # Cчетчик для отсчета каждой 4 цифры в номере карты
            j = 0  # Счетчик для отсчета каждой цифры в номере карты
            array2 = []
            array = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            for characters in operation['from']:
                if characters in array:
                    j += 1
                    i += 1
                    if j in range(7, 13):
                        characters = '*'
                    else:
                        pass
                    if i == 4:
                        characters += ' '
                        array2.append(characters)
                        i = 0
                    else:
                        array2.append(characters)
                else:
                    array2.append(characters)
            operation['from'] = ''.join(array2)
        elif operation['description'] == 'Перевод со счета на счет':
            secure_count_to = 'Счет **' + operation['to'][-4:]
            secure_count_from = 'Счет **' + operation['from'][-4:]
            operation['to'] = secure_count_to
            operation['from'] = secure_count_from
    return data
