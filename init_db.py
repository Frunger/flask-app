import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY,
                      username TEXT NOT NULL)''')
    cursor.execute('INSERT INTO users (username) VALUES (?)', ('fissy',))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
