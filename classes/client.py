import re


class Client:

    def first_name(self):
        first_name = str(input('Podaj imię: '))
        try:
            if re.match("^[A-Z][a-z]{2}[^0-9][^`~!@#$%^&*()_=+{}|,.<>?/]?"):
                return first_name
        except:
            print('Niepoprawne imię!')

    def second_name(self):
        second_name = str(input('Podaj nazwisko: '))
        return second_name

    def city(self):
        city = str(input('Podaj miasto: '))
        return city

    def post_code(self):
        post_code = str(input('Podaj kod pocztowy: '))
        return post_code

    def street(self):
        street = str(input('Podaj ulicę: '))
        return street

    def number_home(self):
        number_home = str(input('Podaj nr domu: '))
        return number_home

    def number_apartment(self):
        number_apartment = str(input('Podaj nr mieszkania: '))
        return number_apartment
