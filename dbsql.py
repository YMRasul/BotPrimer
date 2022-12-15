import sqlite3 as sq
from sqlite3 import Error


class Database:
    def __init__(self, dbFile):
        self.base = sq.connect(dbFile)
        self.cur = self.base.cursor()

    def close(self):
        self.cur.close()
        self.base.close()

    def createTable(self, table):
        with self.base:
            self.cur.execute(table)

    def user_exists(self, user_id):
        with self.base:
            r = self.cur.execute('SELECT * FROM client WHERE user_id == ?', (user_id,)).fetchmany(1)
            return bool(len(r))

    def add_user(self,user_id,user_fio):
        with self.base:
            return self.cur.execute('INSERT INTO client VALUES (?,?,?,?)', (user_id,0, user_fio, 1,))

    def get_users(self):
        with self.base:
            return self.cur.execute('SELECT user_id ,active, fio  FROM   client').fetchall()

    def set_active(self,user_id,active):
        with self.base:
            return self.cur.execute('UPDATE client SET  active==? WHERE user_id==?', (active,user_id))

def create_connection(dbFile):
    ''' Это отделная функция для подключение к базе данных'''
    connection = None
    try:
        connection = sq.connect(dbFile)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
