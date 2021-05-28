from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import User_Registration
from .forms import RegisterForm, ProfileRegisterForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password


def login(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_authenticated:
                auth.login(request, user)
                return HttpResponseRedirect("N/index")
            else:
                return login(request)
        else:
            messages.error(request, "Please enter correct username and password!!!")
            return redirect("/Register")
    else:
        return render(request, "mysite/signup.html")


@login_required
def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


def Register(request):
    if request.method == 'POST':

        profileform = ProfileRegisterForm(data=request.POST)
        form = RegisterForm(data=request.POST)

        un = request.POST.get('username')
        pwd = request.POST.get('password')
        eml = request.POST.get('email')
        mno = request.POST.get('mobile_no')

        try:
            usr = User.objects.get(username=un)
            messages.error(request, "Username already taken!!! Please try another Username.")
        except:
            pass
        if len(un) < 3 or len(eml) < 5 or len(pwd) < 5:
            messages.error(request, "Please input correct data!!")
        elif form.is_valid():
            user = form.save(commit=False)
            user_type = request.POST.get('u_selection')
            if user_type == "Owner":
                if len(mno) < 10:
                    messages.error(request, "Please enter mobile number must be 10 numbers!!")
                    return redirect('Register')
                else:
                    user.password = make_password(user.password)
                    user.save()
                    data = User_Registration(user_type=user_type, mobile_no=mno, user=user)
                    data.save()
                    auth.login(request, user)
                    return redirect('/')
            elif user_type == "Guest":
                user.password = make_password(user.password)
                user.save()
                data = User_Registration(user_type=user_type, mobile_no=None, user=user)
                data.save()
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Enter correct data!! ")
        else:
            messages.error(request, "Invalid form!!")

        context = {"form": profileform, 'mainform': form}
        return render(request, "mysite/signup.html", context)
    else:
        form = ProfileRegisterForm()
        mainform = RegisterForm()
        context = {"form": form, 'mainform': mainform}
        return render(request, "mysite/signup.html", context)
