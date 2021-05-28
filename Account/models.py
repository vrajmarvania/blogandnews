from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Register(models.Model):

class User_Registration(models.Model):
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
    U_Id=models.AutoField

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    ut=(
        ("Guest","Guest"),
        ("Owner","Owner")
    )
    user_type=models.CharField(max_length=20,blank=True,null=True, choices=ut)
    mobile_no=models.CharField(max_length=12,default=None,null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    profilepic = models.ImageField(default="undraw_profile.svg", upload_to="user_profie_pic")

    # profileimage=models.ImageField(upl)

    def __str__(self):
        return self.user.username