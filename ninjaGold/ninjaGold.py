from flask import Flask, render_template, session, redirect, request
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'important'


@app.route('/', methods=['GET'])
def index():
    if 'name' not in session:
        session['name'] = ''

    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def result():
    session['name'] = request.form['name']

    if session['name'] == 'farm':
        session['number'] = random.randint(10, 20)

    elif session['name'] == 'house':
        session['number'] = random.randint(2, 5)

    elif session['name'] == 'cave':
        session['number'] = random.randint(5, 10)

    elif session['name'] == 'casino':
        n = random.randint(0, 1)
        if n == 0:
            session['number'] = random.randint(1, 50)
        else:
            session['number'] = random.randint(-50, -1)
            session['gold'] += session['number']
            session['string'] += 'Entered a Casino and lost ' + str(
                session['number'] * (-1)) + ' golds... ouch ' + '(' + str(datetime.now()) + ')\n'
            return render_template('index.html')

    session['gold'] += session['number']
    session['string'] += 'Earned ' + str(session['number']) + ' golds from the ' + session['name'] + '! ' + '(' + str(
        datetime.now()) + ')\n'
    return render_template('index.html')


@app.route('/reset', methods=['POST'])
def reset():
    session['gold'] = 0
    session['string'] = ''
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
