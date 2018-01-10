from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index),
	url(r'^create$', views.create),
	url(r'^destroyconfirm/(?P<id>\d+)$', views.confirmdelete),
	url(r'^destroy/(?P<id>\d+)$', views.destroy),
	url(r'^comment/(?P<id>\d+)$', views.comment),
	url(r'^createcomment$', views.createcomment),
]