from messages import show_choice_result, get_wrong_message
from user_requests import ask_for_drink_choice

choice_options = 'ДА!'

while True:
    choice = ask_for_drink_choice()
    match choice:
        case 1:
            print(show_choice_result(choice, choice_options))
        case 2:
            print(show_choice_result(choice, choice_options))
        case 3:
            print(show_choice_result(choice, choice_options))
        case _:
            print(get_wrong_message())
            break