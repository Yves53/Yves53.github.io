from flask import Flask, render_template, flash, redirect, url_for, session, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)
app.secret_key = 'very_secret'

# config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5173nsyl'
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MySQL
mysql = MySQL(app)


# Index
@app.route('/')
def index():
    return render_template("index.html")


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('please login first', 'danger')
            return redirect('/login')
    return wrap


@app.route('/messages')
@is_logged_in
def articles():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM messages WHERE user_id = %s", [session['id']])
    messages = cur.fetchall()
    if result > 0:
        return render_template('messages.html', messages=messages)
    else:
        msg = 'No message found'
        cur.close()
        return render_template('messages.html', msg=msg)


@app.route('/message/<string:id>')
@is_logged_in
def message(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM messages WHERE id=%s", [id])
    message = cur.fetchone()
    return render_template("message.html", message=message)


class RegisterForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=50)])
    last_name = StringField('Last Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password',
                           [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')


# user register
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

        flash('Thanks for registering')

        return redirect(url_for('login'))
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
                cur.execute("SELECT first_name FROM users WHERE username = %s", [username])
                r = cur.fetchone()
                session['first'] = r['first_name']
                cur.execute("SELECT id FROM users WHERE username = %s", [username])
                r = cur.fetchone()
                session['id'] = r['id']

                flash('' + session['first'] + ' you are now logged in', 'success')
                cur.close()
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # close connection

        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')


class MessageForm(Form):
    message = TextAreaField('', [validators.Length(min=10)])


class CommentForm(Form):
    comment = TextAreaField('', [validators.Length(min=10)])


# logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


# dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    form = MessageForm(request.form)
    formc = CommentForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()

    # get articles
    result = cur.execute("SELECT * FROM messages WHERE user_id = %s", [session['id']])
    messages = cur.fetchall()
    cur.execute("SELECT * FROM comments WHERE user_id = %s", [session['id']])
    comments = cur.fetchall()

    if result > 0:
        return render_template('dashboard.html', comments=comments, messages=messages, form=form, formc=formc)
    else:
        msg = 'You do not have any messages'
        cur.close()
        return render_template('dashboard.html', msg=msg, comments=comments, messages=messages, form=form)


# Add Article
@app.route('/add_message', methods=['GET', 'POST'])
@is_logged_in
def add_message():
    form = MessageForm(request.form)
    if request.method == 'POST' and form.validate():
        message = form.message.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO messages(message, author, user_id) VALUES(%s, %s, %s) ", (message, session['first'], session['id']))
        mysql.connection.commit()
        cur.close()
        flash('Message successfully created', 'success')
        return redirect(url_for('dashboard'))
    flash('Enter a minimum of 10 characters', 'danger')
    return redirect(url_for('dashboard'))


@app.route('/add_comment/<string:id>', methods=['POST'])
@is_logged_in
def add_comment(id):
    form = MessageForm(request.form)
    formc = CommentForm(request.form)
    if request.method == 'POST' and formc.validate():
        comment = formc.comment.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO comments(comment, author, user_id, message_id ) VALUES(%s, %s, %s, %s)  ", (comment, session['first'], session['id'], [id]))
        mysql.connection.commit()
        cur.close()
        flash('comment successfully created', 'success')
        return redirect(url_for('dashboard'))
    flash('Enter a minimum of 10 characters', 'danger')
    return render_template('dashboard.html',  form=form)


@app.route('/edit_message/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_message(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM messages WHERE id=%s", [id])
    message = cur.fetchone()
    form = MessageForm(request.form)
    form.message.data = message['message']
    if request.method == 'POST' and form.validate():
        message = request.form['message']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE messages SET message=%s WHERE id=%s", (message, id))
        mysql.connection.commit()
        cur.close()
        flash('Message updated', 'success')
        return redirect(url_for('dashboard'))
    return render_template('edit_message.html', form=form)


@app.route('/delete_message/<string:id>', methods=['POST'])
@is_logged_in
def delete_message(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM messages WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash("Message Deleted", 'success')
    return redirect('/dashboard')


if __name__ == '__main__':
    app.run(debug=True)
