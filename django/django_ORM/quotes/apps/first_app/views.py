from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt


def index(request):
    return render(request, "first_app/index.html")

def register(request):
    errors = User.objects.regvalidator(request.POST)

    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/")

    else:
        new_user = User.objects.create(first_name=request.POST["first_name"], alias=request.POST["alias"], email=request.POST["email"], password=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()), birthday = request.POST["bday"])
        request.session["id"] = new_user.id
        # messages.success(request, "Successfully registered!")
        return redirect("/quotes")

def login(request):
    result = User.objects.logvalidator(request.POST)
    print result
    print type(result)

    if result == 'Invalid email or password.':
        messages.error(request, result)
        return redirect("/")
    
    request.session["id"] = result.id
    # messages.success(request, "Successfully loggedin!")
    return redirect("/quotes")

def logout(request):
    del request.session["id"]
    return redirect ("/")

def show_allquotes(request):
    myself = User.objects.get(id=request.session["id"])

    # quotes = Quote.objects.all

    # mines = myself.uploaded_quotes.all()
    
    ''' PREVIOUS VERSION
    # myquotes = Quote.objects.filter(uploader = myself) 
    # mines = []
    # for myquote in myquotes:
    #     mines.append(myquote)
    '''

    notmines = Quote.objects.exclude(id__in = myself.uploaded_quotes.all())

    '''PREVIOUS VERSION
    # notmyquotes = Quote.objects.exclude(uploader = request.session["id"])          
    # notmines = []
    # for notmyquote in notmyquotes:
    #     notmines.append(notmyquote)
    '''

    # favoritequotes = myself.favorite_quotes.all()

    '''PREVIOUS VERSION
    # favorites = Quote.objects.filter(favorited_by = myself)
    # favoritequotes = []
    # for favorite in favorites:
    #     favoritequotes.append(favorite)
    '''

    context = {
        "myself": myself,
        "notmines": notmines,
        # "mines": mines,
        # "favoritequotes" : favoritequotes,
    }
    return render(request, "first_app/allquotes.html", context)

def create_quote(request, id):
    errors = User.objects.quotevalidator(request.POST)

    if errors:
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/quotes")
    # owner = request.POST['owner']
    # quote = request.POST['quote']
    # errors = []

    # if not owner:
    #     errors.append("Quoted by cannot be empty")
    # elif len(owner) < 3:
    #     errors.append("Quoted by must be longer than 3 characters")

    # if not quote:
    #     errors.append("Message cannot be empty")
    # elif len(quote) < 10:
    #     errors.append("Message must be longer than 10 characters")

    # if errors:
    #     for error in errors:
    #         messages.error(request, error)
    else:
        myself = User.objects.get(id=request.session["id"])
        Quote.objects.create(content = request.POST["quote"], owner=request.POST["owner"], uploader = myself)
    return redirect ("/quotes")

def add_favquote(request, id):
    user = User.objects.get(id = request.session["id"])
    favquote = Quote.objects.get(id = id)

    favquote.favorited_by.add(user)

    favquote.save()

    return redirect ("/quotes")

def remove_quote(request, id):
    user = User.objects.get(id = request.session["id"])
    poorquote = Quote.objects.get(id = id)

    poorquote.favorited_by.remove(user)

    return redirect ("/quotes")

def show_userquotes(request, id):
    user = User.objects.get(id = id)

    # quotes = Quote.objects.filter(id__in = user.uploaded_quotes.all())
    # count = len(quotes)

    context = {
        # "quotes" : quotes,
        "user" : user,
        # "count": count
    }
    return render(request, "first_app/profile.html", context)