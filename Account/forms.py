from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User_Registration
from django.db import transaction


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    # def save(self, commit=True):
    #     user=super().save(commit=False)

    #     user.username = self.cleaned_data['username']
    #     user.email = self.cleaned_data['email']
    #     user.password = self.cleaned_data['password']

    #     if commit:
    #         user.save()
    #     return user


class ProfileRegisterForm(forms.ModelForm):
    ut = (
        ('Guest', 'Guest'),
        ('Owner', 'Owner'),
    )
    user_type = forms.ChoiceField(choices=ut, required=True, initial="Guest")
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
                                required=False)

    class Meta:
        model = User_Registration
        fields = ('__all__')

# class LoginForm(forms.ModelForm):

#     # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
#     # password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

#     class Meta:
#         model=User
#         fields=('username', 'password')
