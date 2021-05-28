# Generated by Django 3.1.8 on 2021-05-26 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
        ('Blogs', '0005_remove_blogdata_u_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdata',
            name='U_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Account.user_registration'),
            preserve_default=False,
        ),
    ]
