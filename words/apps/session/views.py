from django.shortcuts import render, redirect
from time import strftime, localtime


# the index function is called when root is visited
def index(request):
    return render(request, 'session/index.html')


def process(request):
    try:
        request.session['big'] = request.POST['big']
    except KeyError:
        request.session['big'] = ''

    request.session['word'] = request.POST['word']
    request.session['color'] = request.POST['color']
    request.session['time'] = strftime("%I:%M%p", localtime())
    request.session['date'] = strftime("%A, %B-%d-%Y", localtime())
    request.session['string'] = request.session['word'] + ' -added at ' + request.session['time'] + ' on ' + request.session['date'] + '\n'
    dictionary = {
        'color': request.session['color'],
        'big': request.session['big'],
        'string': request.session['string']
    }
    request.session['group'].insert(0, dictionary)
    return redirect('/')


def clear(request):
    request.session['group'] = []
    return redirect('/')
