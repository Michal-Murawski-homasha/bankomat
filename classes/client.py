import random
import re

from classes import connection


class Client:

    def __init__(self):
        self.first_name_input = None
        self.first_name = None
        self.second_name_input = None
        self.second_name = None
        self.city_input = None
        self.city = None
        self.post_code_input = None
        self.post_code = None
        self.street_input = None
        self.street = None
        self.number_home_input = None
        self.number_home = None
        self.number_apartment_input = None
        self.number_apartment = None

    def first_name(self, first_name_input, first_name):
        index = 1
        while index == 1:
            self.first_name_input = str(input('Podaj imię: '))
            self.first_name = "^[A-Z][a-z]{2,}[^0-9]{1,}?"
            try:
                if re.search(first_name, first_name_input):
                    return first_name_input
            except TypeError:
                print('Niepoprawne imię!')

    def second_name(self, second_name_input, second_name):
        index = 1
        while index == 1:
            self.second_name_input = str(input('Podaj nazwisko: '))
            self.second_name = "^[A-Z][a-z]{2,}[^0-9]{1,}?"
            try:
                if re.search(second_name, second_name_input):
                    return second_name
            except TypeError:
                print('Niepoprawne nazwisko!')

    def city(self, city_input, city):
        index = 1
        while index == 1:
            self.city_input = str(input('Podaj miasto: '))
            self.city = "^[A-Z][a-z]{2,}|[A-Z][a-z]{2,}([ ]{1}|[-]{1})[A-Z][a-z]?"
            try:
                if re.search(city, city_input):
                    return city
            except TypeError:
                print('Niepoprawna nazwa miasta!')

    def post_code(self, post_code_input, post_code):
        index = 1
        while index == 1:
            self.post_code_input = str(input('Podaj kod pocztowy: '))
            self.post_code = "^[0-9]{2}[-]{1}[0-9]{3}?"
            try:
                if re.search(post_code, post_code_input):
                    return post_code
            except TypeError:
                print("Niepoprawny format kodu pocztowego!")

    def street(self, street_input, street):
        index = 1
        while index == 1:
            self.street_input = str(input('Podaj ulicę: '))
            self.street = "^[A-Z][a-z]{2,}|[A-Z][a-z]{2,}[ ][A-Z][a-z]{2,}?"
            try:
                if re.search(street, street_input):
                    return street
            except TypeError:
                print('Niepoprawna ulica!')

    def number_home(self, number_home_input, number_home):
        index = 1
        while index == 1:
            self.number_home_input = str(input('Podaj nr domu: '))
            self.number_home = "^[0-9]{1,}?"
            try:
                if re.search(number_home, number_home_input):
                    return number_home
            except TypeError:
                print('Nr domu musi być cyfrą!')

    def number_apartment(self, number_apartment_input, number_apartment):
        index = 1
        while index == 1:
            self.number_apartment_input = str(input('Podaj nr mieszkania: '))
            self.number_apartment = "^[0-9]{1}?"
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
