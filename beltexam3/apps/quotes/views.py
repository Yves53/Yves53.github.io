from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    if 'is_logged_in' not in request.session:
        request.session['is_logged_in'] = False
    return render(request, 'quotes/index.html')


def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "You have successfully registered!")
    return redirect('/')


def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    request.session['alias'] = result.alias
    info = User.objects.get(id=request.session['user_id'])
    request.session['name'] = info.name
    request.session['is_logged_in'] = True
    return redirect('/dashboard')


def logout(request):
    request.session['is_logged_in'] = False
    request.session.clear()
    messages.success(request, "Successfully logged out!")
    return redirect('/')


def dashboard(request):
    if not request.session['is_logged_in']:
        messages.success(request, 'Please login first!')
        return redirect('/')
    context = {
        'quotes': Quotes.objects.all().exclude(favorites=User.objects.get(id=request.session['user_id'])),
        'favorites': Quotes.objects.filter(favorites=User.objects.get(id=request.session['user_id'])),
    }
    return render(request, 'quotes/dashboard.html', context)


def add_quote(request):
    if not request.session['is_logged_in']:
        messages.success(request, 'Please login first!')
        return redirect('/')
    request.session['quoted_by'] = request.POST['quoted_by']
    request.session['quote'] = request.POST['quote']
    if len(request.session['quoted_by']) < 3:
        messages.success(request, 'The field "quoted by" cannot be less than 3 characters')
        return redirect('/dashboard')
    if len(request.session['quote']) < 10:
        messages.success(request, 'The message cannot be less than 10 characters')
        return redirect('/dashboard')
    Quotes.objects.create(quoted_by=request.session['quoted_by'], quote=request.session['quote'], usr=User.objects.get(id=request.session['user_id']))
    return redirect('/dashboard')


def add_to_list(request, number):
    Quotes.objects.get(id=number).favorites.add(User.objects.get(id=request.session['user_id']))
    return redirect('/dashboard')


def remove_from_list(request, number):
    Quotes.objects.get(id=number).favorites.remove(User.objects.get(id=request.session['user_id']))
    return redirect('/dashboard')


def user_quotes(request, number):
    context = {
        'quotes': Quotes.objects.filter(usr_id=number),
        'user': User.objects.get(id=number).alias,
        'count': Quotes.objects.filter(usr_id=User.objects.get(id=number)).count()
    }
    return render(request, 'quotes/user_quotes.html', context)
