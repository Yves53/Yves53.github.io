from django.shortcuts import render, HttpResponse, redirect


# the index function is called when root is visited
def index(request):
    return render(request, 'survey_form/index.html')


def process(request):
    if 'time' not in request.session:
        request.session['time'] = 1
    else:
        request.session['time'] += 1

    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['name'] = request.POST['name']
    return redirect('/result')


def result(request):
    return render(request, 'survey_form/result.html')
