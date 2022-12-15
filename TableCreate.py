from dbsql import Database


def createTables(db):
    tables = [
        '''CREATE TABLE IF NOT EXISTS client (user_id INTEGER PRIMARY KEY NOT NULL, phone INTEGER,fio TEXT,active INTEGER)''',
        '''CREATE TABLE IF NOT EXISTS org (id INTEGER PRIMARY KEY NOT NULL, nam)'''
    ]
    try:
        baza = Database(db)
        print('Подключение к базе данных и Создание таблиц')
        # Создание таблиц
        for tab in tables:
            baza.createTable(tab)
    finally:
        baza.close()

