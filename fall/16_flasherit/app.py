# Ayham Alnasser & Vishwaa Sofat & Kiran Vuksanaj (Save the Turtles)
# SoftDev pd1
# K15 - Do I Know You?
# 2019-10-02

from flask import Flask, render_template, request, session, redirect, url_for, flash
from data import secret

app = Flask(__name__)
app.secret_key = secret.main()


@app.route('/', methods=["GET", "POST"])
def hello():
    if 'username' in session:
        if 'admin' in session['username']:
            return redirect(url_for("alr_log_in"))
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def log_in():
    if 'username' not in session:
        session['username'] = request.form.get('username')
        session['password'] = request.form.get('password')
    if 'admin' != session['username']:
        error = "Incorrect User"  # yoinked right from the docs
        flash(error, 'error')
    if 'pass' != session['password']:
        error = "Bad password"
        flash(error, 'error')
    elif 'admin' == session['username'] and 'pass' == session['password']:
        return render_template('welcome.html', username=session['username'])
    session.pop('username')
    session.pop('password')
    return render_template('login.html')


@app.route('/login', methods=['GET'])
def alr_log_in():
    return render_template('welcome.html',
                           username=session['username'])


@app.route('/logout',methods=["POST"])
def log_out():
    button = request.form['Log_out']
    if button == 'Log Out':
        session.pop('username')
        session.pop('password')
    return redirect(url_for("hello"))


if __name__ == '__main__':
    app.debug = True
    app.run()
