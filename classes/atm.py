from classes.connection import Connection


class Atm(Connection):
    def login_atm(self):
        input('Podaj nr karty: ')
        input('Podaj PIN: ')
        sql = 'SELECT * FROM konto_klienta'
        data = []
        stmt = Connection.connected()
        stmt.execute(sql, data)
        result = stmt.fetchall()
        print(result)
        for x in result:
        	print(x)
