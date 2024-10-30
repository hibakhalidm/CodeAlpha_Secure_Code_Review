from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)
DATABASE = 'test.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def index():
    return "Welcome to the Vulnerable App!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)
        user = conn.execute(query).fetchone()
        if user:
            return "Logged in as {}".format(username)
        else:
            return "Login failed"
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/user/<username>')
def user_profile(username):
    return render_template_string("Hello, {{username}}!", username=username)

if __name__ == '__main__':
    app.run(debug=True)
