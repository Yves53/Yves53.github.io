from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime


# the index function is called when root is visited
def index(request):
    context = {
        'date': strftime("%A, %B-%d-%Y", localtime()),
        'time': strftime("%I:%M%p", localtime())
    }
    return render(request, 'time/index.html', context)

