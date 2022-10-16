from classes import connection


class Atm:
    @staticmethod
    def login_atm():
        input('Podaj nr karty: ')
        input('Podaj PIN: ')
        sql = 'SELECT * FROM konto_klienta'
        data = []
        stmt = connection.Connection.connected()
        stmt.execute(sql, data)
        result = stmt.fetchall()
        print(result)
        for x in result:
        	print(x)
