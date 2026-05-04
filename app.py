import sqlite3
from flask import Flask, request

app = Flask(__name__)

# VULNERABILITY 1 - B105: Hardcoded Password
# Risk: Anyone with GitHub access can see your real DB password
DB_PASSWORD = "super_secret_password_123"


@app.route('/login')
def login():
    user = request.args.get('user')

    # VULNERABILITY 2 - B608: SQL Injection via f-string
    # Attack: user = "admin' OR '1'='1" --> dumps ALL users!
    query = f"SELECT * FROM users WHERE username = '{user}'"

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return "Query executed!"


@app.route('/admin')
def admin():
    # VULNERABILITY 3 - B104 (triggered below in app.run)
    # Shown here: host='0.0.0.0' = accepts from ANY IP on network
    return "Admin panel!"


if __name__ == "__main__":
    # VULNERABILITY 4 - B201: debug=True exposes interactive Python debugger
    # VULNERABILITY 3 - B104: host='0.0.0.0' = exposed to entire internet
    app.run(debug=True, host='0.0.0.0')
