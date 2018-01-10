from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.messages import error


def index(request): 
	context = {
		"courses" : Course.objects.all(),
		"description" : Description.objects.all(),
	}
	print "INDEX", context
	return render(request, 'first_app/index.html', context)


def create(request):
	errors = Course.objects.validate(request.POST)
	if errors:
		for err in errors:
			error(request, err)
	else:
		course = Course.objects.create(
			name = request.POST['name']
		)
		description =  Description.objects.create(
			text = request.POST['description'],
			belongsto = course
		)
		print "********COURSE*****", course

	return redirect("/")


def confirmdelete(request,id):
	context = {
		"coursetobedeleted" : Course.objects.get(id = id),
	}
	return render(request, 'first_app/confirmdelete.html', context)

def destroy(request,id):
	deletecourse = Course.objects.get(id = id)
	deletecourse.delete()
	return redirect('/')

def comment(request, id):
	course = Course.objects.get(id = id)
	comment = Comment.objects.filter(belongsto = id)
	description = Description.objects.filter(belongsto = id)
	context = {
		"course" : course,
		"description" : description,
		"comment" : comment
	}
	print "====COMMENT=========", context
	return render(request, "first_app/comments.html", context)

def createcomment(request):
	print "bas", request.POST['id']
	courseid = request.POST['id']
	course = Course.objects.get(id = courseid)
	comment = Comment.objects.create(text = request.POST['comment'], belongsto = course)
	return redirect ('/comment/{}'.format(courseid))


