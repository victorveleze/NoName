import pymysql

class Database():
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            db = 'users'
        )

        self.cursor = self.connection.cursor()
        print("Connection successful!")


    def __del__(self):
        self.connection.close()
        print("Disconnected!")
