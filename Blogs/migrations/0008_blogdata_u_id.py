# Generated by Django 3.1.8 on 2021-05-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0007_remove_blogdata_u_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdata',
            name='u_id',
            field=models.IntegerField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]
