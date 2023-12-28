from datetime import datetime

def formated_date(date):
    """Функция преобразует формат времени в нужный (через точку) день, месяц, год"""
    short_date = date[:10]
    return datetime.strptime(short_date, '%Y-%m-%d').strftime('%d.%m.%Y')


def test_formated_date():
    date_input = "2023-12-28T09:17:22"
    expected_output = "28.12.2023"
    result = formated_date(date_input)
    assert result == expected_output, f"Ожидания:  {expected_output}, реальность: {result}"

print(test_formated_date())
