import re


class Client:

    @staticmethod
    def first_name():
        first_name_input = str(input('Podaj imię: '))
        first_name = "^[A-Z][a-z]{2}[^0-9]?"
        index = 0
        while index == 0:
            try:
                if re.search(first_name, first_name_input):
                    return first_name
                index = 1
            except TypeError:
                index = 0
                print('Niepoprawne imię!')

    @staticmethod
    def second_name():
        second_name = str(input('Podaj nazwisko: '))
        return second_name

    @staticmethod
    def city():
        city = str(input('Podaj miasto: '))
        return city

    @staticmethod
    def post_code():
        post_code = str(input('Podaj kod pocztowy: '))
        return post_code

    @staticmethod
    def street():
        street = str(input('Podaj ulicę: '))
        return street

    @staticmethod
    def number_home():
        number_home = str(input('Podaj nr domu: '))
        return number_home

    @staticmethod
    def number_apartment():
        number_apartment = str(input('Podaj nr mieszkania: '))
        return number_apartment
