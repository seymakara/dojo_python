from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index),
    url(r'^register$', views.register_page),
    url(r'^signin$', views.signin_page),
    url(r'^process_register$', views.register),
    url(r'^process_signin$', views.signin),
    url(r'^logout$', views.logout),
    url(r'^dashboard$', views.user_dashboard),
    url(r'^dashboard/admin$', views.admin_dashboard), #for admin
    url(r'^users/new$', views.add_user_page), #for admin
    url(r'^process_new$', views.add_user), #for admin
    url(r'^users/remove/(?P<id>\d+)$', views.remove_user), #for admin
    url(r'^users/edit/(?P<id>\d+)$', views.edit_user_page), #for admin
    url(r'^process/edit/(?P<id>\d+)/admin$', views.edit_user), #for admin
    url(r'^process/edit_pw/(?P<id>\d+)/admin$', views.edit_user_pw), #for admin
    url(r'^users/edit$', views.edit_profile_page), #for user
    url(r'^process/users/edit$', views.edit_profile), #for user
    url(r'^process/users/edit_pw$', views.edit_profile_pw), #for user
    url(r'^users/remove/(?P<id>\d+)$', views.remove_user), #for admin
    url(r'^users/show/(?P<id>\d+)$', views.show_profile_page), 
    url(r'^process_message/(?P<id>\d+)$', views.process_message), 
    url(r'^process_comment/(?P<id>\d+)$', views.process_comment), 
    

]