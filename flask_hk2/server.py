from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninja')
def ninja():
    return render_template('ninja.html')


@app.route('/ninja/<st>')
def ninjas(st):
    if st == 'orange':
        return render_template('michelangelo.html')
    if st == 'blue':
        return render_template('leonardo.html')
    if st == 'red':
        return render_template('raphael.html')
    if st == 'purple':
        return render_template('donatello.html')
    else:
        return render_template('notapril.html')


app.run(debug=True)
