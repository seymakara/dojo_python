from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime, localtime
from django.utils.crypto import get_random_string

def index(request):
    context ={
    "time": strftime("%H:%M:%S", localtime()),
    "date": strftime("%Y-%m-%d", localtime())
    }
    return render(request,'time_display_app/index.html', context)


