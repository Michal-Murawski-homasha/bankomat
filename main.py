import self as self

import classes.client

print('1. Założyć nowe konto')
print('2. Skorzystać z bankomatu')
print('2. Skorzystać z wpłatomatu')
number = int(input('Wybierz numer akcji, którą chcesz wykonać: '))

if number == 1:
    classes.client.Client.first_name(self)
    classes.client.Client.second_name(self)
    classes.client.Client.city(self)
    classes.client.Client.post_code(self)
    classes.client.Client.street(self)
    classes.client.Client.number_home(self)
    classes.client.Client.number_apartment(self)
elif number == 2:
    print('2')
elif number == 3:
    print('3')