from flask import Flask, render_template, session, request, flash, redirect

app = Flask(__name__)
app.secret_key = 'important'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/user', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print request.form['name']
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')

    if len(request.form['location']) < 1:
        flash("Location cannot be empty!")
        return redirect('/')

    if len(request.form['language']) < 1:
        flash("language cannot be empty!")
        return redirect('/')

    return redirect('/show')


@app.route('/show')
def user():
    return render_template('result.html', name = session['name'], location = session['location'], language = session['language'], comment = session['comment'])


if __name__ == '__main__':
    app.run(debug=True)
