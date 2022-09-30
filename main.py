import sys

import self as self

import classes.client

print('1. Założyć nowe konto')
print('2. Skorzystać z bankomatu')
print('2. Skorzystać z wpłatomatu')
print('4. Wyjść z programu')

index = 1
while index == 1:
    try:
        number = int(input('Wybierz numer akcji, którą chcesz wykonać: '))
        if number == 1:
            classes.client.Client.first_name()
            classes.client.Client.second_name()
            classes.client.Client.city()
            classes.client.Client.post_code()
            classes.client.Client.street()
            classes.client.Client.number_home()
            classes.client.Client.number_apartment()
            classes.client.Client.creat_number_acount()
            print()
            classes.client.Client.creat_login()
            classes.client.Client.creat_pin()
            print()
        elif number == 2:
            print('2')
        elif number == 3:
            print('3')
        elif number == 4:
            sys.exit()
    except ValueError:
        print('Nr się nie zgadza! Wybierz 1 lub 2 lub 3.')