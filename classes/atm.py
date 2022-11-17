from classes.connection import Connection


class Atm(Connection):
    def login_atm(self):
        self.number_cart = input('Podaj nr karty: ')
        self.pin_code = input('Podaj PIN: ')
        sql = 'SELECT * FROM konto_klienta WHERE numerKonta = ' + self.number_cart
        data = [1]
        mysql_connect = self.mydb
        mysql_connect.execute(sql, data)
        result = mysql_connect.fetchall()
        for row in result:
            print("Hospital Id:", row[0])
