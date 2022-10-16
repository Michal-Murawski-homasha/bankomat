from classes.connection import Connection


class Atm(Connection):
    def login_atm(self):
        self.number_cart = input('Podaj nr karty: ')
        self.pin_code = input('Podaj PIN: ')
        sql = 'SELECT * FROM kontoKlienta'
        data = []
        stmt = Connection.connected(self)
        stmt.execute(sql, data)
        result = stmt.fetchall()
        print(result)
        for x in result:
            print(x)
