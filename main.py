import self as self

import classes.client

print('1. Założyć nowe konto')
print('2. Skorzystać z bankomatu')
print('2. Skorzystać z wpłatomatu')


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
    elif number == 2:
        print('2')
    elif number == 3:
        print('3')
except ValueError:
    print('Nr się nie zgadza! Wybierz 1 lub 2 lub 3.')