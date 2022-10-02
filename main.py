import sys

import self as self

import classes.client


index = 1

while index == 1:
    try:
        print('1. Założyć nowe konto')
        print('2. Skorzystać z bankomatu')
        print('2. Skorzystać z wpłatomatu')
        print('4. Wyjść z programu')
        print()

        number = int(input('Wybierz numer akcji, którą chcesz wykonać: '))
        print()

        if number == 1:
            classes.client.Client.first_name()
            classes.client.Client.second_name()
            classes.client.Client.city()
            classes.client.Client.post_code()
            classes.client.Client.street()
            classes.client.Client.number_home()
            classes.client.Client.number_apartment()
            classes.client.Client.creat_number_acount()
            print('--------------------')
            classes.client.Client.creat_login()
            classes.client.Client.creat_pin()
            classes.client.Client.create_account()
            print('--------------------')
        elif number == 2:
            print('2')
            print()
        elif number == 3:
            print('3')
            print()
        elif number == 4:
            sys.exit()
        else:
            print('Wybierz numer od 1 do 4')
            print()
    except ValueError:
        print('Nr się nie zgadza! Wybierz 1 lub 2 lub 3.')