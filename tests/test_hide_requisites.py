def hide_requisites(requisites: str):
    """Функция маскирует карты и счета"""
    parts = requisites.split()
    number = parts[-1]

    if requisites.lower().startswith('счет'):
        hided_number = f"**{number[-4:]}"
    else:
        hided_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

    return ' '.join(parts[:-1]) + " " + hided_number


def test_hide_requisites_bank_account():
    # Тестирование маскировки для счета
    input_data = "Счет 12345678"
    expected_result = "Счет **5678"
    assert hide_requisites(input_data) == expected_result

def test_hide_requisites_credit_card():
    # Тестирование маскировки для номера карты
    input_data = "Карта 1234567890123456"
    expected_result = "Карта 1234 56** **** 3456"
    assert hide_requisites(input_data) == expected_result
