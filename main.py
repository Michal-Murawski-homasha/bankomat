import sys

import self as self

import classes.client
import classes.atm
import classes.deposit


if __name__ == '__main__':
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
                client = classes.client.Client()
                print(client.test())
                print('--------------------')
                client.first_name()
                client.second_name()
                client.city()
                client.post_code()
                client.street()
                client.number_home()
                client.number_apartment()
                client.create_account_number()
                print('--------------------')
                client.creat_login()
                client.creat_pin()
                client.create_account()
                print('--------------------')
            elif number == 2:
                atm_service = classes.atm.Atm()
                atm_service.login_atm()
                print()
            elif number == 3:
                deposit_service = classes.deposit.Deposit()
                deposit_service.deposit_amount()
                print()
            elif number == 4:
                sys.exit()
            else:
                print('Wybierz numer od 1 do 4')
                print()
        except ValueError:
            print('Nr się nie zgadza! Wybierz 1 lub 2 lub 3.')