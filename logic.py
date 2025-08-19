import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS errors1 (
            id INTEGER,
            name TEXT)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS errors2 (
            id INTEGER,
            name TEXT)''')
    

    def get_id1(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute('SELECT MAX(id) FROM errors1')
        x = cur.fetchall()
        x = x[0]
        x = x[0]
        if x == None:
            x = 0
        return x
    
    def get_id2(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute('SELECT MAX(id) FROM errors2')
        x = cur.fetchall()
        x = x[0]
        x = x[0]
        if x == None:
            x = 0
        return x

    def add_request1(self, id, name):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('INSERT INTO errors1 VALUES (?, ?)', (id, name))
            conn.commit()
    def add_request2(self, id, name):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('INSERT INTO errors2 VALUES (?, ?)', (id, name))
            conn.commit()
    
    def delete_id1(self, id):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute(f'DELETE FROM errors1 WHERE id={id}')
            conn.commit()
    def delete_id2(self, id):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute(f'DELETE FROM errors2 WHERE id={id}')
            conn.commit()


if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_tables()
    a = manager.get_id1()
    b = manager.get_id2()
    print(a, b)