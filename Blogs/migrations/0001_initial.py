# Generated by Django 3.1.8 on 2021-05-26 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(blank=True, max_length=20, null=True)),
                ('blog_content', models.CharField(default=None, max_length=12, null=True)),
                ('blog_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
