from datetime import date

from rest_framework import serializers

from . import models
from .models import blogdata
from Account.models import User_Registration


class blogdataSerializer(serializers.Serializer):
    # U_id = serializers.RelatedField(source='User_Registration', read_only=True)
    blog_date = serializers.DateField(("Date"), default=date.today)
    u_id=serializers.IntegerField()

    blog_title=serializers.CharField(max_length=100)
    blog_content=serializers.CharField(max_length=1000)



    def create(self, validate_data):
        return blogdata.objects.create(**validate_data)



class blogdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.blogdata
        fields = ('id', 'blog_date', 'u_id', 'blog_title', 'blog_content')
