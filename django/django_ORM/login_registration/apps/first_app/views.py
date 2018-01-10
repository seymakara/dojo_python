from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
from .models import *
import bcrypt

  # the index function is called when root is visited
def index(request):
    return render(request, "first_app/index.html")

def success(request):
    try:
        context = {
            "user": User.objects.get(id=request.session["id"])
        }
        return render(request, "first_app/success.html", context)
    except:
        return redirect('/')


def register(request):
    errors = User.objects.regvalidator(request.POST)
    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/")
    else:
        new_user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()))
        request.session["id"] = new_user.id
        messages.success(request, "Successfully registered!")
        return redirect("/success")

def login(request):
    result = User.objects.logvalidator(request.POST)
    print result
    print type(result)

    if result == 'Invalid email or password.':
        messages.error(request, result)
        return redirect("/")
    
    request.session["id"] = result.id
    messages.success(request, "Successfully loggedin!")
    return redirect("/success")