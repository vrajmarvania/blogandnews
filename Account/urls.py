from django.conf.urls import url
from django.urls import path, include
from . import views
# from Account.views import signin,login,Register
from django.contrib.auth import views as auth_views
urlpatterns=[
    path("Register",views.Register, name="Register"),
    path("login",views.login, name="login"),

    path("logout", views.logout, name="logout"),



]