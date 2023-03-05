import json
from datetime import datetime

def data_list(json_data):
    """" Функция получает данные с расширением .json
     и возвращает его значения как словарь Python
    """

    data = json.loads(json_data)
    return data


def filter_data(data, filtered_empty_from=False):
    """
    Получает данные в формате list и возвращает те данные,
    которые по ключу "state" имеют значения "EXECUTED"
    """

    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def sort_data(data, count_last_values=5):
    """
     Функция принимает данные в формате list и возвращает отсортированные в обратном порядке данные,
     в колличестве указанных в переменной count_last_values, по умолчанию равной 5
    """

    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last_values]


def format_data(data):
    """Функция форматирует данные до нужного формата
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб."""

    formated_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        if "from" in row:
            sender = row["from"].split()
            sender_bill = sender.pop(-1)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
            sender_info = "".join(sender)
        else:
            sender_bill = ""
            sender_info = ""

        recipient = f"**{row['to'][-4:]}"
        amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'

        formated_data.append(f"""
{date} {description}
{sender_info} {sender_bill} -> Счёт {recipient}
{amount}
        """)

    return formated_data