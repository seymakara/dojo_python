from django.conf.urls import url
from . import views           
urlpatterns = [     
    url(r'^main$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^quotes/create/(?P<id>\d+)$', views.create_quote),
    url(r'^quotes/remove/(?P<id>\d+)$', views.remove_quote),
    url(r'^quotes$', views.show_allquotes),
    url(r'^quotes/add/(?P<id>\d+)$', views.add_favquote),
    url(r'^users/(?P<id>\d+)$', views.show_userquotes),
    url(r'^$', views.index),
]
