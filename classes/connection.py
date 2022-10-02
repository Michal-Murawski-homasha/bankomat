import mysql.connector


class Connection:
    @staticmethod
    def connected():
        mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bankomat"
        )
