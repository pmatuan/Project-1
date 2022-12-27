from datetime import timedelta
from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "Project-1-1-tcejorP"
app.permanent_session_lifetime = timedelta(seconds=10)


@app.route('/')
@app.route('/home')
def home():
    return redirect(url_for("login"))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_name = request.form["token_id"]
        if user_name == "glpat-A4wxGBzLAgBxyYBueyS6":
            session["user"] = "Tuan"
            session.permanent = True
            return redirect(url_for("hello_user", name=user_name))
    if "user" in session:
        name = session["user"]
        return f"<h1> Hello {name}</h1>"
    return render_template('login.html')


@app.route('/user')
def hello_user():
    if "user" in session:
        name = session["user"]
        return f"<h1> Hello {name}</h1>"
    else:
        return redirect(url_for("login"))


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
