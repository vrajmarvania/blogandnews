from django.contrib import admin
from .models import User_Registration
# from django.contrib.auth.models import User
# Register your models here.
@admin.register(User_Registration)
class UserRegistration(admin.ModelAdmin):
    class Meta:
        model = User_Registration
        list_display=['__all__']

# admin.site.register(User_Registration)