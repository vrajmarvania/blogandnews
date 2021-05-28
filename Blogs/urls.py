"""BN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from django.urls import include, path

from Blogs import views

router = routers.DefaultRouter()
router.register('blogCreate', views.blogdataViewSet)

urlpatterns = [
   path('addblog',views.addblog,name='index'),
   path('Blogindex', views.Blogindex, name='Blogindex'),
   path('submit',views.blog_add ,name='add'),
   path('fullblog/<int:id>', views.fullblog, name='fullblog'),
   path('del/<int:id>', views.dell, name='fullblog'),

   path('Deskbord', views.Deskbord, name='Deskbord'),
   path('site_admin', views.site_admin, name='site_admin'),

   path('', include(router.urls)),

   path('blogDeatils/', views.blogList.as_view(),name='blogDeatils'),
   path('blogDeatils/<int:pk>', views.blogDeatils.as_view()),
   path('', include('rest_framework.urls', namespace='rest_framework'))

]

