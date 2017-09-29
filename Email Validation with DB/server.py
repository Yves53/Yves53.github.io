from flask import Flask, redirect, session, flash, request, render_template, url_for
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'super_important'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5173nsyl'
app.config['MYSQL_DB'] = 'emails_validator'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


class RegisterForm(Form):
    email = StringField('email', [validators.Length(min=6, max=50)])


@app.route('/checker', methods=['POST'])
def checker():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO emails(email) VALUES(%s)", [email])
        mysql.connection.commit()
        cur.close()
        return redirect('/show')
    else:
        error = 'Invalid email'
        return render_template('index.html', error=error)


@app.route("/show")
def show():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM emails")
    data = cur.fetchall()
    return render_template('success.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
