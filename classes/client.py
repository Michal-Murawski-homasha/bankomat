import random
import re

from classes.connection import Connection


class Client(Connection):
    def first_name(self):
        index = 1
        while index == 1:
            self.first_name_input = str(input('Podaj imię: '))
            self.first_name_validate = "^[A-Z][a-z]{1,}[^0-9]{1,}?"
            try:
                if re.search(self.first_name_validate, self.first_name_input):
                    return 0
            except TypeError:
                print('Niepoprawne imię!')
                return 1

    def second_name(self):
        index = 1
        while index == 1:
            self.second_name_input = str(input('Podaj nazwisko: '))
            self.second_name_validate = "^[A-Z][a-z]{2,}[^0-9]{1,}?"
            try:
                if re.search(self.second_name_validate, self.second_name_input):
                    return 0
            except TypeError:
                print('Niepoprawne nazwisko!')
                return 1

    def city(self):
        index = 1
        while index == 1:
            self.city_input = str(input('Podaj miasto: '))
            self.city_validate = "^[A-Z][a-z]{2,}|[A-Z][a-z]{2,}([ ]{1}|[-]{1})[A-Z][a-z]?"
            try:
                if re.search(self.city_validate, self.city_input):
                    return 0
            except TypeError:
                print('Niepoprawna nazwa miasta!')
                return 1

    def post_code(self):
        index = 1
        while index == 1:
            self.post_code_input = str(input('Podaj kod pocztowy: '))
            self.post_code_validate = "^[0-9]{2}[-]{1}[0-9]{3}?"
            try:
                if re.search(self.post_code_validate, self.post_code_input):
                    return 0
            except TypeError:
                print("Niepoprawny format kodu pocztowego!")
                return 1

    def street(self):
        index = 1
        while index == 1:
            self.street_input = str(input('Podaj ulicę: '))
            self.street_validate = "^[A-Z][a-z]{2,}|[A-Z][a-z]{2,}[ ][A-Z][a-z]{2,}?"
            try:
                if re.search(self.street_validate, self.street_input):
                    return 0
            except TypeError:
                print('Niepoprawna ulica!')
                return 1

    def number_home(self):
        index = 1
        while index == 1:
            self.number_home_input = str(input('Podaj nr domu: '))
            self.number_home_validate = "^[0-9]{1,}?"
            try:
                if re.search(self.number_home_validate, self.number_home_input):
                    return 0
            except TypeError:
                print('Nr domu musi być cyfrą!')
                return 1

    def number_apartment(self):
        index = 1
        while index == 1:
            self.number_apartment_input = str(input('Podaj nr mieszkania: '))
            self.number_apartment_validate = "^[0-9]{1}?"
            try:
                if re.search(self.number_apartment_validate, self.number_apartment_input):
                    return 0
            except TypeError:
                print('Nr domu musi być cyfrą! (0 jeżeli nie posiada)!')
                return 1

    def create_account_number(self):
        index = 1
        print('Twój numer konto: ', end='')
        while index <= 26:
            self.rand_number = random.randint(0, 9)
            self.print_number = print(self.rand_number, end='')
            self.account_number = [self.rand_number]
            index += 1
        print()

    def creat_login(self):
        index = 1
        print('Twój login: ', end='')
        while index <= 4:
            print(random.randint(0, 9), end='')
            index += 1
        print()

    def creat_pin(self):
        pin = input('Utwórz 4 cyfrowy PIN: ')

    def create_account(self):
        mysql_connect = Connection.connected(self)
        query = "INSERT INTO dane_klienta (imieKlienta, nazwiskoKlienta, miasto, kodPocztowy, ulica, numerDomu, numerMieszkania)" \
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = [self.first_name_input, self.second_name_input, self.city_input, self.post_code_input,
                  self.street_input, self.number_home_input, self.number_apartment_input]
        mysql_connect.execute(query, values)
        self.mydb.commit()
