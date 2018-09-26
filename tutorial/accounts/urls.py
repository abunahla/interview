from django.conf.urls import url
from accounts import views as accounts_views
from django.contrib.auth.views import (login, logout,
 password_reset, password_reset_done, password_reset_confirm
)
from . import views

urlpatterns =[
    url(r'^password_reset/', password_reset, name='password_reset'),
    url(r'^password_reset_done/', password_reset, name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)=(?P<token>.+)', password_reset_confirm, name='password_reset_confirm'),
    url(r'^login/$', login,{'template_name':'accounts/login.html'}),
    url(r'^logout/$', logout,{'template_name':'accounts/logout.html'}),
    url(r'^register/$', accounts_views.register, name='register.html'),
    url(r'^profile/$', accounts_views.view_profile, name='profile.html'),
    url(r'^profile/edit/$', accounts_views.edit_profile, name='profile_edit.html'),
    
 
]
