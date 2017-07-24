from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'trainingapp'

urlpatterns=[
    url(r'^$',views.login_user,name='home'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login_user,name='login_user'),
    url(r'^logout/$',views.logout_user,name='logout_user'),
    # url(r'^login/$','django.contrib.auth.views.login',name='login'),
    # url(r'^logout/$',auth_views.logout,{'next_page': 'login'},name='logout'),

]