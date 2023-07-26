from user_requests import *
from messages import *

a = 'ДА!'
b = a
c = b
res = c

while True:
    choice = select_choice()
    if choice == 1:
        print(msg(choice, res))
    elif choice == 2:
        print(msg(choice, res))
    elif choice == 3:
        print(msg(choice, res))
    else:
        print(msg_wrong())

#
