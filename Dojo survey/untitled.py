from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = 'important'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
