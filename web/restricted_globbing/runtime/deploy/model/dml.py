import sqlite3

def findUser(id, pw):
    with sqlite3.connect("user.db") as conn:
        cur = conn.cursor()
        # 파라미터는 '?'를 사용하여 바인딩
        query = "SELECT * FROM users WHERE username=? AND password=?"
        
        # No SQL Injection ^^
        cur.execute(query, (id, pw))
        res = cur.fetchone()
    return res

def join(id, pw):
    with sqlite3.connect("user.db") as conn:
        cur = conn.cursor()
        # 파라미터는 '?'를 사용하여 바인딩
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        
        # No SQL Injection ^^
        cur.execute(query, (id, pw))
