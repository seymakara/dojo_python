from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
from django.shortcuts import get_object_or_404
from .models import *
import bcrypt

def index(request):
    return render(request, "first_app/index.html")

def register_page(request):
    return render(request, "first_app/register.html")

def signin_page(request):
    return render(request, "first_app/signin.html")

def register(request):
    errors = User.objects.regvalidator(request.POST)

    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/register")

    else:
        if len(User.objects.all()) == 0:
            new_user = User.objects.create(user_level = 9, first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()))
            request.session["id"] = new_user.id
            return redirect("/dashboard/admin")
        else:
            new_user = User.objects.create(user_level = 1, first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()))
            request.session["id"] = new_user.id
            return redirect("/dashboard")

def signin(request): 
    result = User.objects.logvalidator(request.POST)

    if result == 'Invalid email or password.':
        messages.error(request, result)
        return redirect("/signin")
    else:
        request.session["id"] = result.id
        if result.user_level == 9:
            return redirect("/dashboard/admin")
        else:
            return redirect("/dashboard")

def logout(request):
    if "id" in request.session:

        del request.session["id"]
        return redirect ("/")

    return redirect ("/")

def admin_dashboard(request):
    if "id" not in request.session:
        return redirect ('/')

    user = User.objects.get(id = request.session["id"])
    if user.user_level == 9:
        users = User.objects.all()
        context = {
            "users" : users
        }
        return render(request, "first_app/admin_dashboard.html", context)
    else:
        return HttpResponse('<h3>Page not found</h3>')

def user_dashboard(request):
    if "id" in request.session:
        users = User.objects.all()
        context = {
            "users" : users
        }
        return render(request, "first_app/user_dashboard.html", context)
    return redirect ('/')

def add_user_page(request):
    if "id" not in request.session:
        return redirect ('/')

    user = User.objects.get(id = request.session["id"])
    if user.user_level == 9:
        return render(request, "first_app/add_user.html")
    else:
        return HttpResponse('<h3>Page not found</h3>')

def add_user(request):
    errors = User.objects.regvalidator(request.POST)

    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/users/new")

    User.objects.create(user_level = 1, first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()))
    return redirect("/users/new")

def edit_user_page(request, id):
    if "id" not in request.session:
        return redirect("/")

    user = User.objects.get(id=request.session["id"])
    
    if user.user_level == 9:
        user = User.objects.get(id=id)
        context = {"user" : user}
        return render(request, "first_app/edit_user_admin.html", context)
    else:
        return HttpResponse('<h3>Page not found</h3>')

def edit_user(request, id):
    if "id" not in request.session:
        return redirect("/")

    user = User.objects.get(id = request.session["id"])

    if user.user_level == 9:
        user = User.objects.get(id=id)

        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email=request.POST["email"]

        if request.POST["user_level"] == "normal":
            user.user_level = 1
        elif request.POST["user_level"] == "admin":
            user.user_level = 9
        user.save()
        return redirect ("/users/edit/{}".format(id))
    else:
        return HttpResponse('<h3>Page not found</h3>')

def edit_user_pw(request, id):
    if "id" not in request.session:
        return redirect("/")

    user = User.objects.get(id = request.session["id"])

    if user.user_level == 9:
        errors = User.objects.pw_changevalidator(request.POST)
        if len(errors):
            for error in errors.itervalues():
                messages.error(request, error)
            return redirect("/users/edit/{}".format(id))

        user = User.objects.get(id=id)

        user.password=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
        user.save()
        return redirect ("/users/edit/{}".format(id))
    else:
        return HttpResponse('<h3>Page not found</h3>')

def edit_profile_page(request):
    if "id" in request.session:
        user = User.objects.get(id=request.session["id"])
        context = {"user" : user}
        return render(request, "first_app/edit_profile_user.html", context)
    return redirect("/")

def edit_profile(request):
    if "id" not in request.session:
        return redirect("/")

    user = User.objects.get(id=request.session["id"])

    user.first_name = request.POST["first_name"]
    user.last_name = request.POST["last_name"]
    user.email=request.POST["email"]
    user.save()
    return redirect ("/users/edit")

def edit_profile_pw(request):
    if "id" not in request.session:
        return redirect("/")

    errors = User.objects.pw_changevalidator(request.POST)
    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/users/edit")

    user = User.objects.get(id=request.session["id"])
    user.password=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
    user.save()
    return redirect ("/users/edit")

def remove_user(request, id):
    if "id" not in request.session:
        return redirect("/")

    user = User.objects.get(id=request.session["id"])
    
    if user.user_level == 9:
        user = User.objects.get(id=id)
        user.delete()
        return redirect ("/dashboard/admin")
    else:
        return HttpResponse('<h3>Page not found</h3>')

def show_profile_page(request, id):
    if "id" not in request.session:
        return redirect("/")
    user = User.objects.get(id = id)
    messages = Message.objects.filter(receiver = user.id)
    comments = Comment.objects.all()
    context = {
        'user': user,
        'messages':messages,
        'comments':comments,
    }
    return render(request, "first_app/show_profile.html", context)

def process_message(request, id):
    if "id" not in request.session:
        return redirect("/")
    
    user_sender = User.objects.get(id = request.session["id"])
    user_receiver = User.objects.get(id = id)
    Message.objects.create(message = request.POST["message"], sender = user_sender, receiver = user_receiver)
    return redirect ("/users/show/{}".format(id))

def process_comment(request, id):
    if "id" not in request.session:
        return redirect("/")

    user = User.objects.get(id = request.session["id"])
    messageid = request.POST.get('messageid')
    messageofcomment = Message.objects.get(id = messageid)
    Comment.objects.create(comment = request.POST["comment"], sender = user, message = messageofcomment)
    return redirect ("/users/show/{}".format(id))
    













