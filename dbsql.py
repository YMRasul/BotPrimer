import sqlite3 as sq


class Database:
    def __init__(self, dbFile):
        self.base = sq.connect(dbFile)
        self.cur = self.base.cursor()

    def createTable(self, table):
        self.base.execute(table)
        self.base.commit()

    def user_exists(self, user_id):
        with self.base:
            r = self.base.execute('SELECT * FROM client WHERE user_id == ?', (user_id,)).fetchmany(1)
            return bool(len(r))

    def add_user(self,user_id,user_fio):
        with self.base:
            return self.base.execute('INSERT INTO client VALUES (?,?,?,?)', (user_id,0, user_fio, 1,))

    def get_users(self):
        with self.base:
            return self.base.execute('SELECT user_id ,active  FROM   client').fetchall()

    def set_active(self,user_id,active):
        with self.base:
            return self.base.execute('UPDATE client SET  active==? WHERE user_id==?', (active,user_id))