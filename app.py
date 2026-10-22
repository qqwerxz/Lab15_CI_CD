def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b



def divide(a, b):
    """Делит первое число на второе."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b