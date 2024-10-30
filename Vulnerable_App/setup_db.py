import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
c.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")
conn.commit()
conn.close()
