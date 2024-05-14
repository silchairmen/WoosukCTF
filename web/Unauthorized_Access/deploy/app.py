from flask import Flask, render_template, request, redirect, url_for, session, abort
import sqlite3
import csv

app = Flask(__name__)
app.secret_key = 'FAKE_SECRET'  

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        DROP TABLE users;
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rank INTEGER NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    txt_file_path = 'users.txt'

    users = []
    with open(txt_file_path, 'r') as txtfile:
        for line in txtfile:
            rank, username, password = line.strip().split(',')
            users.append((rank, username, password))

    cursor.executemany('INSERT INTO users (rank, username, password) VALUES (?, ?, ?)', users)

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        password = session['password']
        rank = session['rank']
        return render_template('loginindex.html', username=username, rank=rank)
    else:
        return render_template('index.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    session.pop('password', None)
    session.pop('rank', None)
    return '''
    <script>
        alert("로그아웃 성공!");
        window.location.href = "/";
    </script>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT rank, password FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    
    conn.close()

    if result is not None:
        rank, db_password = result
        if db_password == password:
            session['username'] = username
            session['password'] = password
            session['rank'] = rank
            return '''
            <script>
                alert("로그인 성공!");
                window.location.href = "/";
            </script>
            '''
    return '''
    <script>
        alert("로그인 실패!");
        window.location.href = "/";
    </script>
    '''

@app.route('/guest', methods=['POST'])
def guest_login():
    session['username'] = "guest"
    session['password'] = "guest"
    session['rank'] = 0
    return '''
    <script>
        alert("게스트 로그인 성공!");
        window.location.href = "/";
    </script>
    '''

def escape_string(s):
    forbidden_words = ["update", "drop", "delete", "create", "insert", "select", "union"]
    s_lower = s.lower()
    for word in forbidden_words:
        if word in s_lower:
            abort(403)
    return s_lower

@app.route('/register', methods=['POST'])   c
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    escaped_username = escape_string(username)
    escaped_password = escape_string(password)
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    try:
        query = f'INSERT INTO users (rank, username, password) VALUES (0,"{escaped_username}", "{escaped_password}")'
        cursor.execute(query)
        conn.commit()
        
        query = "SELECT COUNT(*) FROM users WHERE rank >= 1"
        cursor.execute(query)
        total = cursor.fetchone()[0]
        conn.commit()
        
        if total >= 1:
            query = "DELETE FROM users WHERE username != 'guest'"
            cursor.execute(query)
            conn.commit()
            conn.close()
            with open('flag.txt', 'r') as f:
                flag_content = f.read().strip()
            return f'성공하셨군요..? Flag: {flag_content}'
        conn.close()
        return '회원가입이 완료되었습니다.'
    except sqlite3.IntegrityError:
        conn.close()
        return '이미 존재하는 사용자입니다.'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug=False)
