import random
import re

from classes import connection


class Client:

    def first_name(self):
        index = 1
        while index == 1:
            first_name_input = str(input('Podaj imię: '))
            first_name = "^[A-Z][a-z]{2,}[^0-9]{1,}?"
            try:
                if re.search(first_name, first_name_input):
                    return first_name
            except TypeError:
                print('Niepoprawne imię!')

    def second_name(self):
        index = 1
        while index == 1:
            second_name_input = str(input('Podaj nazwisko: '))
            second_name = "^[A-Z][a-z]{2,}[^0-9]{1,}?"
            try:
                if re.search(second_name, second_name_input):
                    return second_name
            except TypeError:
                print('Niepoprawne nazwisko!')

    def city(self):
        index = 1
        while index == 1:
            city_input = str(input('Podaj miasto: '))
            city = "^[A-Z][a-z]{2,}|[A-Z][a-z]{2,}([ ]{1}|[-]{1})[A-Z][a-z]?"
            try:
                if re.search(city, city_input):
                    return city
            except TypeError:
                print('Niepoprawna nazwa miasta!')

    def post_code(self):
        index = 1
        while index == 1:
            post_code_input = str(input('Podaj kod pocztowy: '))
            post_code = "^[0-9]{2}[-]{1}[0-9]{3}?"
            try:
                if re.search(post_code, post_code_input):
                    return post_code
            except TypeError:
                print("Niepoprawny format kodu pocztowego!")

    def street(self):
        index = 1
        while index == 1:
            street_input = str(input('Podaj ulicę: '))
            street = "^[A-Z][a-z]{2,}|[A-Z][a-z]{2,}[ ][A-Z][a-z]{2,}?"
            try:
                if re.search(street, street_input):
                    return street
            except TypeError:
                print('Niepoprawna ulica!')

    def number_home(self):
        index = 1
        while index == 1:
            number_home_input = str(input('Podaj nr domu: '))
            number_home = "^[0-9]{1,}?"
            try:
                if re.search(number_home, number_home_input):
                    return number_home
            except TypeError:
                print('Nr domu musi być cyfrą!')

    def number_apartment(self):
        index = 1
        while index == 1:
            number_apartment_input = str(input('Podaj nr mieszkania: '))
            number_apartment = "^[0-9]{1}?"
            try:
                if re.search(number_apartment, number_apartment_input):
                    return number_apartment
            except TypeError:
                print('Nr domu musi być cyfrą! (0 jeżeli nie posiada)!')

    def creat_number_acount(self):
        index = 1
        print('Twój numer konto: ', end='')
        while index <= 26:
            print(random.randint(0, 9), end='')
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

    def create_account(self, first_name, second_name, city, post_code, street, number_home, number_apartment):
        query = "INSERT INTO dane_klienta (imieKlienta, nazwiskoKlienta, miasto, kodPocztowy, ulica, numerDomu, numerMieszkania) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = [first_name, second_name, city, post_code, street, number_home, number_apartment]
        mysql_connect = connection.Connection.connected()
        mysql_connect.execute(query, values)
        connection.Connection.connected()
