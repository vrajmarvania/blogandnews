# Generated by Django 3.1.8 on 2021-05-26 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0004_blogdata_u_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdata',
            name='U_id',
        ),
    ]
