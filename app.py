# app.py
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# SECURITY RISK: Hardcoded credentials (Bandit will flag B105)
DB_PASSWORD = "super_secret_password_123"

@app.route('/login')
def login():
    user = request.args.get('user')
    # SECURITY RISK: SQL Injection (Bandit will flag B608)
    query = f"SELECT * FROM users WHERE username = '{user}'"
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return "Query executed!"

if __name__ == "__main__":
    # SECURITY RISK: Debug mode enabled (Bandit will flag B201)
    app.run(debug=True, host='0.0.0.0')
