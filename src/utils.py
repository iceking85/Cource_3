import json
from datetime import datetime
from config import OPERATIONS_FILE_PATH


def get_all_operations():
    '''Функция извлекает данные из файла operations.json и возвращает их'''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def filter_executed_operations():
    """Функция для фильтрации словарей через метон get, а также функция возвращает словари с EXECUTED """
    all_operations = get_all_operations()
    executed_operations = [operation for operation in all_operations if operation.get('state') == 'EXECUTED']
    return executed_operations


sorted_dict = sorted(filter_executed_operations(), key=lambda x: x['date'], reverse=True)
five_first_operations = sorted_dict[:5]
"""Сортирует словари по датам и в переменной хранятся самые свежие 5 словрей"""

def formated_date(date):
    """Функция преобразует формат времени в нужный (через точку)день, месяц, год"""
    short_date = date[:10]
    return datetime.strptime(short_date, '%Y-%m-%d').strftime('%d.%m.%Y')


def hide_requisites(requisits: str):
    """Функция маскирует карты и счета"""
    parts = requisits.split()
    number = parts[-1]
    if requisits.lower().startswith('счет'):
        hided_number = f"**{number[-4:]}"
    else:
        hided_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    return ' '. join(parts[:-1]) + " " + hided_number

def get_formated_operations(sorted_list):
    """Функция для вывода выше перечисленных словарей"""
    formatted_operations = []
    for sorted_dict in sorted_list:
        date = formated_date(sorted_dict['date'])
        type_operations = sorted_dict['description']
        line_one_output = f"{date} {type_operations}"
        if sorted_dict.get('from'):
            hided_from = hide_requisites(sorted_dict.get('from'))
        else:
            hided_from = '->'
        hided_to = hide_requisites(sorted_dict.get('to'))
        line_two_output = f"{hided_from} {hided_to}"
        amount = sorted_dict['operationAmount']['amount']
        currency = sorted_dict['operationAmount']['currency']['name']
        line_three_output = f"{amount} {currency}"
        formatted_operations.append(f"{line_one_output}\n{line_two_output}\n{line_three_output}\n")
    return formatted_operations