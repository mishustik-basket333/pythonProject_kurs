from functions import *


def main():
    # Вводится название документа из которого берутся данные
    ADRESS_DATA = "operations.json"

    # Вводится желаемое колличество вывода операций
    COUNT_LAST_VALUES = 5

    # Используется в функции filter_data. При значении True отсекает операции, где нет значения "from"
    FILTERED_EMPTY_FROM = True

    # Открывает данные из адреса файла в переменной ADRESS_DATA и записывает в переменную data
    with open(ADRESS_DATA, "r") as fafafa:
        data = fafafa.read()

    # Выполняются основные функции для преобразования исходных данных
    data = data_list(data)
    data = filter_data(data, FILTERED_EMPTY_FROM)
    data = sort_data(data, COUNT_LAST_VALUES)
    data = format_data(data)

    # Вывод данных на экран абзацами через пробел
    for row in data:
        print(row)


main()
