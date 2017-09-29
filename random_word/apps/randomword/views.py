from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


# the index function is called when root is visited
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1

    context = {

        'count': request.session['counter'],
        'string': get_random_string(length=14)
    }
    return render(request, 'randomword/index.html', context)


def reset(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] = 0

    return redirect('/randomword')
