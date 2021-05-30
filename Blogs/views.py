from django.http import response
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser

from .models import blogdata
from .serializers import  blogdataSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import requests
import json
from django.shortcuts import render, redirect

from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics


from .models import  blogdata
from .serializers import  blogdataSerializer
def site_admin(request):
    if request.session.has_key('ID'):


        data = blogdata.objects.all()
        u_name = request.user

        print(data)
        param = {'data': data, 'u_name': u_name}
        print(param)
        return render(request,'site_admin.html',param)
    else:
        return render(request, 'mysite/signup.html')

def addblog(request):
    if request.session.has_key('ID'):

        if request.method =="POST":
            print("1")
            u_id=request.user.id
            print("}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
            print(u_id)
            blog_title = request.POST.get('blog_title')
            blog_content = request.POST.get('blog_content')
            url = 'http://127.0.0.1:8000/B/submit'
            data = {
                'u_id':u_id,
                'blog_title':blog_title,
                'blog_content':blog_content,
            }
            print(data)
            print("2")

            json_data = json.dumps(data)
            print(json_data)
            print("3")

            r = requests.post(url=url, data=json_data)
            print(r)
            print("4")

            data = r.json()
            print(data)
            u_name = request.user
            param={'data':data,'u_name':u_name}
            return render(request, "blogform.html",param)
        u_name = request.user

        param={'u_name':u_name}
        return render(request, "blogform.html",param)

    else:
      return render(request, 'mysite/signup.html')



def Blogindex(request):
    if request.session.has_key('ID'):

        data=blogdata.objects.all()
        print(data)
        param={'data':data}
        return render(request,'blog.html',param)
    else:
        return render(request, 'mysite/signup.html')


import json

# Create your views here.


@csrf_exempt
def blog_add(request):
    print("------------++")
    if request.method == "POST":
        print("in ")
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        print("6")
        print(pythondata)
        print('7')
        serializer = blogdataSerializer(data=pythondata)
        print(serializer)
        print('8')

        if serializer.is_valid():
            print("iinnn")
            serializer.save()
            print("okkk bro")
            res = {'msg': "Data Created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

    # if request.method == "GET":
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     id = pythondata.get('id', None)
    #     if id is not None:
    #         stu = blogdata.objects.get(id=id)
    #         serializer = blogdataSerializer(stu)
    #         json_data = JSONRenderer().render(serializer.data)
    #         return HttpResponse(json_data, content_type="application/json")
    #     stu = blogdata.objects.all()
    #     serializer = blogdataSerializer(stu, many=True)
    #     json_data = JSONRenderer().render(serializer.data)
    #     return HttpResponse(json_data, content_type="application/json")

def fullblog(request,id):
    if request.session.has_key('ID'):

        data = blogdata.objects.filter(id=id)
        print(data[0])
        param = {'data': data[0]}
        print(param)
        return render(request, 'fullblog.html', param)

    else:
        return render(request, 'mysite/signup.html')


def Deskbord(request):
    if request.session.has_key('ID'):

        id = request.user.id

        data = blogdata.objects.filter(u_id=id)
        u_name = request.user

        print(data)
        param = {'data': data, 'u_name': u_name}
        print(param)

        return render(request, 'Deskbord.html', param)

    else:
        return render(request, 'mysite/signup.html')


def dell(request,id):
    if request.session.has_key('ID'):

        print(id)
        blogdata.objects.filter(id=id).delete()

        return redirect('/B/Deskbord')

    else:
        return render(request, 'mysite/signup.html')






class blogdataViewSet(viewsets.ModelViewSet):
    queryset = blogdata.objects.all()
    serializer_class = blogdataSerializer
    permission_classes = [permissions.IsAuthenticated]

class blogDeatils(generics.RetrieveUpdateDestroyAPIView):
    queryset = blogdata
    serializer_class = blogdataSerializer


class blogList(generics.ListAPIView):
    queryset = blogdata.objects.all()
    serializer_class = blogdataSerializer