from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^likes_books$', views.index)     
]
