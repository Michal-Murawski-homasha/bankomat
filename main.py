import self as self

import classes.client

print('1. Założyć nowe konto')
print('2. Skorzystać z bankomatu')
print('2. Skorzystać z wpłatomatu')
number = int(input('Wybierz numer akcji, którą chcesz wykonać: '))

if number == 1:
    str(classes.client.Client.first_name(self))
    str(classes.client.Client.second_name(self))
    str(classes.client.Client.city(self))
    str(classes.client.Client.post_code(self))
    str(classes.client.Client.street(self))
    str(classes.client.Client.number_home(self))
    str(classes.client.Client.number_apartment(self))
elif number == 2:
    print('2')
elif number == 3:
    print('3')