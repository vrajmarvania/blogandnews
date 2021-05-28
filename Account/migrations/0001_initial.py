# Generated by Django 3.1.5 on 2021-05-08 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, choices=[('Guest', 'Guest'), ('Owner', 'Owner')], max_length=20, null=True)),
                ('mobile_no', models.CharField(default=None, max_length=12, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=30, null=True)),
                ('profilepic', models.ImageField(default='undraw_profile.svg', upload_to='user_profie_pic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]