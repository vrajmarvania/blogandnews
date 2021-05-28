from django.urls import path
from . import views
# from Account.views import signin,login,Register

urlpatterns=[
    path("Register",views.Register, name="Register"),
    path("",views.login, name="login"),



    # path("Forgot_password", views.Forgot_password, name="login"),

]