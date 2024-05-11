from flask import Flask, render_template, request, redirect, url_for, session , flash
from datetime import timedelta
import sqlite3
import secrets
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
app.permanent_session_lifetime = timedelta(hours=24)

import sqlite3

def initialize_db():
    with sqlite3.connect('bank.db') as conn:
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS accounts (account_number TEXT PRIMARY KEY, balance REAL)''')

        c.execute("SELECT COUNT(*) FROM accounts")
        c.execute("DELETE FROM accounts")
        c.execute("INSERT INTO accounts (account_number, balance) VALUES ('admin', 999999999)")
        conn.commit()


initialize_db()

def get_db():
    conn = sqlite3.connect('bank.db')
    return conn

@app.route('/')
def index():
    if 'account_number' not in session:
        session['account_number'] = secrets.token_hex(16)
        c = get_db()
        c.execute("INSERT INTO accounts (account_number, balance) VALUES (?, ?)", (session['account_number'], 50000))
        c.commit()
        c.close()
        return render_template('index.html', bankid=session['account_number'])
    elif 'account_number' in session:
        return render_template('index.html', bankid=session['account_number'])
    else:
        return render_template('index.html', bankid="no Session")

    
    
    
@app.route('/transfer', methods=['POST'])
def transfer():
    from_account = request.form.getlist('from-account')
    to_account = request.form['to-account']
    amount = int(request.form['amount'])
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()

    if 'admin' in from_account[0]:
        conn.close()
        return render_template('index.html', result="Invalid account number.")
    
    if (len(from_account) > 1):
        from_account = from_account[-1]
    else:
        from_account = from_account[0]
    
    if amount < 0:
        flash('Invalid Amount', 'error')
        conn.close()
        return redirect(url_for('index'))

    c.execute("SELECT balance FROM accounts WHERE account_number = ?", (from_account,))
    from_account_data = c.fetchone()
    print(from_account_data)
    if from_account_data:
        from_account_balance = from_account_data[0]
        if from_account_balance >= amount:
            c.execute("SELECT balance FROM accounts WHERE account_number = ?", (to_account,))
            to_account_data = c.fetchone()
            if to_account_data:
                
                new_from_balance = from_account_balance - amount
                new_to_balance = to_account_data[0] + amount
                if (from_account=='admin'):
                    c.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_to_balance, to_account))
                else:    
                    c.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_from_balance, from_account))
                    c.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_to_balance, to_account))
                conn.commit()
                result = "Transfer successful!"

                c.execute("SELECT SUM(balance) FROM accounts")
                if from_account_balance >= 100000000:
                    result += " You can buy the FLAG product. go to /buy-flag"
            else:
                result = "Invalid recipient account."
        else:
            result = "Insufficient funds in the source account."
    else:
        result = "Invalid source account."

    conn.close()
    return redirect('/')

@app.route('/check-balance', methods=['POST'])
def check_balance():
    data = request.get_json()
    if not data or 'account' not in data:
        return "Invalid request", 400

    account_number = data.get('account')
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
    account_data = c.fetchone()
    conn.close()

    if account_data:
        return f"Account balance: ${account_data[0]}"
    else:
        return "Invalid account number", 404

@app.route('/buy-flag')
def buy_flag():
    acc_num = session.get('account_number')
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute("SELECT balance FROM accounts WHERE account_number = ?", (acc_num,))
    total_balance = c.fetchone()[0]
    conn.close()

    if total_balance >= 100000000:
        try:
            with open("./FLAG", "r") as f:
                flag = f.read().strip()
            return render_template('index.html', result=f"Congratulations! You have purchased the FLAG product. The flag is: {flag}")
        except FileNotFoundError:
            return render_template('index.html', result="Error: FLAG file not found.")
    else:
        return render_template('index.html', result="Insufficient funds to purchase the FLAG product.")
    
if __name__ == '__main__':
    app.run(debug=True)