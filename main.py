def add_everything_up(a, b):
    """
    Складывает числа (int, float) и строки (str), обрабатывая разные типы с использованием исключений.

    Args:
        a: Первое значение (число или строка).
        b: Второе значение (число или строка).

    Returns:
        Результат сложения (число или строка в случае разных типов).
        Возвышает TypeError, если a и b разные типы (число и строка).
    """
    try:
        if isinstance(a, str) and isinstance(b, str):
            return a + b
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return a + str(b)
        elif isinstance(a, (int, float)) and isinstance(b, str):
            return str(a) + b
        else:
            raise TypeError("Невозможно сложить значения разных типов (кроме строк).")
    except TypeError as e:
        return f"Ошибка: {e}"


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

