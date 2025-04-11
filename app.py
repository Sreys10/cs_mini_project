# app.py
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    products = []
    if request.method == 'POST':
        search = request.form['search']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # 🚨 VULNERABLE CODE - no input sanitization!
        query = f"SELECT * FROM products WHERE name LIKE '%{search}%'"
        c.execute(query)

        products = c.fetchall()
        conn.close()

    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
