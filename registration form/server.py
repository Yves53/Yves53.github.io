from flask import Flask, render_template, session, request, flash, redirect
from validate_email import validate_email
app = Flask(__name__)
app.secret_key = 'important'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/user', methods=['POST'])
def result():
    is_valid = validate_email(request.form['email'])
    if is_valid is not True:
        flash("Enter a valid email!")
        return redirect('/')

    if request.form['firstName'].isalpha() is not True:
        flash("Fist name cannot be empty or contain number!")
        return redirect('/')

    if request.form['lastName'].isalpha() is not True:
        flash("Last name cannot be empty or contain number!")
        return redirect('/')

    if len(request.form['pswd']) < 8:
        flash("Password has to be more than 8 characters long!")
        return redirect('/')

    if request.form['pswdc'] != request.form['pswd']:
        flash("Password do not match!")
        return redirect('/')

    return redirect('/show')


@app.route('/show')
def user():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
