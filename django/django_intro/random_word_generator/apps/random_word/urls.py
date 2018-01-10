from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^generate$', views.generate),
    url(r'^random_word/reset$', views.reset),
    url(r'^$', views.index),
    url(r'^random_word$', views.index)
]