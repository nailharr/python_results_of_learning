def show_choice_result(choice, result):
    """
    Выводит на экран выбор пользователя и соответствующий результат.

    Args:
        choice (str): Выбор пользователя.
        result (str): Результат, связанный с выбором.

    Returns:
        str: Строка с результатом.
    """
    print(f"Ваш выбор: {choice}")
    return f"Результат: {result}\n-------------"


def get_wrong_message():
    """
    Возвращает сообщение с инструкцией о повторном выборе.

    Returns:
        str: Сообщение с инструкцией.
    """
    return "Жми на ссылку, потом повтори выбор:\nhttps://natribu.org/"