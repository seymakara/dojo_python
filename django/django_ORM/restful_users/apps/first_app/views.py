from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
from .models import User

def index(request):
    users = User.objects.all()
    context = {
        "users" : users,
    }
    return render(request, 'first_app/index.html', context)

def new(request):
    return render(request, "first_app/new.html")

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message)
        
        return redirect('/users/new')
        
    user = User.objects.create(
        first_name=request.POST['firstname'], 
        last_name = request.POST['lastname'], 
        email = request.POST['email'])
    print "JUST ADDED THESE THINGS"
    return redirect('/users/{}'.format(user.id))

def show(request, id):
    user = User.objects.get(id = id)
    context = {
      "user" : user,
    }
    print "__________USER__________"
    print user
    return render(request, 'first_app/show.html', context)

def edit(request, id):
    user = User.objects.get(id = id)
    context = {
      "user" : user,
    }
    print "------CONTEXT-------"
    print context
    return render(request, 'first_app/edit.html', context)

def update(request, id):
    errors = User.objects.update_validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message)
        
        return redirect('/users/{}/edit'.format(id))

    tobeupdated = User.objects.get(id = id)

    tobeupdated.first_name = request.POST['firstname']
    tobeupdated.last_name = request.POST['lastname']
    tobeupdated.email = request.POST['email']
    tobeupdated.save()

    return redirect ('/users/{}'.format(id))

def destroy(request,id):
    tobedeleted = User.objects.get(id = id)

    tobedeleted.delete()

    return redirect ('/users')








