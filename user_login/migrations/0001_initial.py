# Generated by Django 2.1.dev20180309075957 on 2018-03-17 19:33

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
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill1', models.CharField(max_length=16)),
                ('skill2', models.CharField(max_length=16)),
                ('skill3', models.CharField(max_length=16)),
                ('extraSkills', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pic', models.ImageField(upload_to='profile_pics')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='skills',
            name='userName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_login.UserProfile'),
        ),
    ]
