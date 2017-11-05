import os
from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
from flask import send_from_directory

app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template("login.html", error=error)

@app.route('/index2', methods=['GET', 'POST'])
def index2():
    return render_template("index2.html")

#giving port address from cloud9 to run
if __name__ == '__main__':
   app.run(
       debug=True,
       port = int(os.getenv('PORT', 8080)),
       host = os.getenv('IP', '0.0.0.0')
   )
