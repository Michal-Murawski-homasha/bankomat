from classes.connection import Connection


class Atm(Connection):
    def login_atm(self):
        self.number_cart = input('Podaj nr karty: ')
        self.pin_code = input('Podaj PIN: ')
        sql = 'SELECT * FROM kontoKlienta'
        data = []
        mysql_connect = self.mydb
        mysql_connect.execute(sql, data)
        result = mysql_connect.fetchall()
        print(result)
        for x in result:
            print(x)
