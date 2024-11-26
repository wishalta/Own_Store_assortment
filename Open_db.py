import mysql.connector

class open_db():
    def __init__(self):
        self.connectDB()

    def connectDB(self):
           self.conn = mysql.connector.connect(
               host="127.0.0.1",
               user='root',
               password='',
               database="shop_test"
           )

    def close(self):
        self.conn.close()