from user_requests import *
from messages import *

a = 'ДА!'
b = a
c = b

while True:
    choice = select_choice()
    if choice == 1:
        print(msg(choice, a))
    elif choice == 2:
        print(msg(choice, b))
    elif choice == 3:
        print(msg(choice, c))
    else:
        print(msg_wrong())
