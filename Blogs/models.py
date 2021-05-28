from datetime import date

from django.db import models

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Register(models.Model):
import sys
sys.path.append("..")
from Account.models import User_Registration


class blogdata(models.Model):
    # U_id = models.ForeignKey(User_Registration, on_delete=models.CASCADE)
    blog_date = models.DateField(("Date"), default=date.today)
    u_id=models.IntegerField()

    # user=models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=100)
    blog_content=models.CharField(max_length=1000)




