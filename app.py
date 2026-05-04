import os
import sqlite3

from flask import Flask, request


app = Flask(__name__)

# FIX 1 - B105: Load from environment variable, never hardcode
# Local dev: export DB_PASSWORD="yourpassword"
# AWS prod:  use Secrets Manager or SSM Parameter Store
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")


@app.route('/login')
def login():
    user = request.args.get('user', '')

    # FIX 2 - B608: Parameterized query prevents SQL Injection
    # '?' is a safe placeholder — sqlite3 handles escaping automatically
    query = "SELECT * FROM users WHERE username = ?"

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query, (user,))
    return "Query executed!"


@app.route('/admin')
def admin():
    return "Admin panel - localhost only!"


if __name__ == "__main__":
    # FIX 3 - B201: Debug mode read from env var, False by default in prod
    flask_debug = os.environ.get("FLASK_DEBUG", "false")
    debug_mode = flask_debug.lower() == "true"

    # FIX 4 - B104: Bind to localhost only
    # Use Nginx or AWS ALB as reverse proxy for external traffic
    app.run(debug=debug_mode, host='127.0.0.1')
