import mysql.connector as connection
from Util.DBPropertyUtil import PropertyUtil
class dbConnection():
    def init(self):
        pass
    def open(self):
        try:
            l = PropertyUtil.getPropertyString()
            self.conn = connection.connect(host="localhost", database="petpals", username="root", password="Pujan@23")
            if self.conn:
                print("--Database Is Connected--")
                self.stmt = self.conn.cursor()
        except Exception as e:
            print(e)

    def close(self):
        try:
            self.conn.close()
            print('Connection Closed.')
        except Exception as e:
            print(e)