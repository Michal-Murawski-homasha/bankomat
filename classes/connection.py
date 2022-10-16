import mysql.connector


class Connection:
    def connected(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bankomat"
        )

    def test(self):
        return 'Połączono z bankomatem'
