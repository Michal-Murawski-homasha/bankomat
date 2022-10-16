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
                set_first_name = classes.client.Client.first_name()
                set_second_name = classes.client.Client.second_name()
                set_city = classes.client.Client.city()
                set_post_code = classes.client.Client.post_code()
                set_street = classes.client.Client.street()
                set_number_home = classes.client.Client.number_home()
                set_number_apartment = classes.client.Client.number_apartment()
                classes.client.Client.creat_number_acount()
                print('--------------------')
                classes.client.Client.creat_login()
                classes.client.Client.creat_pin()
                classes.client.Client.create_account(set_first_name, set_second_name, set_city, set_post_code, set_street, set_number_home, set_number_apartment)
                print('--------------------')
            elif number == 2:
                classes.atm.Atm.login_atm()
                print()
            elif number == 3:
                classes.deposit.Deposit.deposit_amount()
                print()
            elif number == 4:
                sys.exit()
            else:
                print('Wybierz numer od 1 do 4')
                print()
        except ValueError:
            print('Nr się nie zgadza! Wybierz 1 lub 2 lub 3.')