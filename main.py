from src.utils import secure_for_card_number


def main():
    """Основная функция, реализующая вывод информации в необходимом виде"""
    data = secure_for_card_number()
    for operations in data:
        if operations['description'] == 'Открытие вклада':
            print(f"{operations['date']} {operations['description']}\n {operations['to']}\n"
                  f"{operations['operationAmount']['amount']} {operations['operationAmount']['currency']['name']}")
        else:
            print(f"{operations['date']} {operations['description']}\n{operations['from']} -> {operations['to']}\n"
                  f"{operations['operationAmount']['amount']} {operations['operationAmount']['currency']['name']}")


main()
