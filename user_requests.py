def ask_for_drink_choice():
    """
    Запрашивает у пользователя выбор по поводу питья сегодня.

    Возможные варианты выбора:
    1 - Да
    2 - Нет
    3 - Позже

    Returns:
        int: Выбор пользователя (1, 2 или 3).
    """
    options = {
        1: "Да",
        2: "Нет",
        3: "Позже"
    }

    while True:
        print("Будете пить сегодня?")
        for key, value in options.items():
            print(f"{key} - {value}")

        try:
            choice = int(input("Введите 1, 2 или 3: "))
            if choice in options:
                return choice
            else:
                print("Пожалуйста, введите 1, 2 или 3.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число (1, 2 или 3).")
