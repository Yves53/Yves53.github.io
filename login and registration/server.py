from flask import Flask, redirect, session, flash, request, render_template, url_for
from passlib.hash import sha256_crypt
from wtforms import Form, StringField, PasswordField, validators
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'super_important'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5173nsyl'
app.config['MYSQL_DB'] = 'login_and_registration'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


class RegisterForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=50)])
    last_name = StringField('Last Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = StringField('Password',
                           [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(first_name, last_name, email, username, password) VALUES(%s, %s, %s, %s, %s)",
                    (first_name, last_name, email, username, password))
        # Commit to DB
        mysql.connection.commit()

        # close connection
        cur.close()

        flash(u'Thanks for registering', 'success')

        return redirect(url_for('show'))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # passed
                session['logged_in'] = True
                session['username'] = username
                cur.execute("SELECT last_name FROM users WHERE username = %s", [username])
                r = cur.fetchone()
                session['last'] = r['last_name']


                flash(u'you are now logged in', 'success')
                cur.close()
                return redirect(url_for('show'))
            else:
                flash(u'Invalid login', 'error')
                return render_template('login.html')
            # close connection

        else:
            flash(u'username not found', 'error')
            return render_template('login.html')

    return render_template('login.html')


@app.route('/show')
def show():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
