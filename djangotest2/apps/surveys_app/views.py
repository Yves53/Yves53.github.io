from django.shortcuts import render, HttpResponse, redirect


def surveys(request):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)


def new(request):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)
