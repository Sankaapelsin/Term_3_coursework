import json
import datetime


def loads():
    """Открываем файл с данными и читаем его"""
    with open(r"C:\Users\User\Desktop\PyCharm_Projects\Term's_work_3\data\operations.json", "r", encoding='utf8') as file:
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


def for_from_card_and_account_coding():
    """Функция для шифрования (скрытия) данных карты или
        счета отправителя, возвращает данные об последних пяти
        операциях с зашифрованныии данными и отформатированной датой"""
    data = date_formatting()
    for operation in data:
        if operation['description'] == 'Открытие вклада':
            pass
        else:
            if 'Счет' in operation['from']:
                secure_account = 'Счет **' + operation['from'][-4:]
                operation['from'] = secure_account
            else:
                card_number = operation['from'].split()[-1]
                i = 0
                j = 1
                array = []
                for character in card_number:
                    if j == 4:
                        if 5 < i < 12:
                            character = '*'
                        j = 0
                        character = character + ' '
                    elif 5 < i < 12:
                        character = '*'
                    i += 1
                    j += 1
                    array.append(character)
                secured_number = ''.join(array)
                operation['from'] = ' '.join(operation['from'].split()[:-1]) + ' ' + secured_number
    return data


def securing_card_and_account_to():
    """Функция для шифрования (скрытия) данных карты или
    счета получателя, возвращает данные об последних пяти
    операциях с зашифрованныии данными и отформатированной датой"""
    data = for_from_card_and_account_coding()
    for operation in data:
        if 'Счет' in operation['to']:
            secure_account = 'Счет **' + operation['to'][-4:]
            operation['to'] = secure_account
        else:
            card_number = operation['to'].split()[-1]
            i = 0
            j = 1
            array = []
            for character in card_number:
                if j == 4:
                    if 5 < i < 12:
                        character = '*'
                    j = 0
                    character = character + ' '
                elif 5 < i < 12:
                    character = '*'
                i += 1
                j += 1
                array.append(character)
            secured_number = ''.join(array)
            operation['to'] = ' '.join(operation['to'].split()[:-1]) + ' ' + secured_number
    return data


def function_for_showing():
    """Функция ,которая возвращает данные об последних пяти операциях
      с зашифрованныии данными и отформатированной датой"""
    data = securing_card_and_account_to()
    for operations in data:
        if operations['description'] == 'Открытие вклада':
            print(f"{operations['date']} {operations['description']}\n{operations['to']}\n"
                  f"{operations['operationAmount']['amount']} {operations['operationAmount']['currency']['name']}\n")
        else:
            print(f"{operations['date']} {operations['description']}\n"
                  f"{operations['from']} --> {operations['to']}\n"
                  f"{operations['operationAmount']['amount']} "
                  f"{operations['operationAmount']['currency']['name']}\n")
