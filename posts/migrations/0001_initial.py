# Generated by Django 2.0.9 on 2018-12-05 08:41

from django.conf import settings
from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('liked', models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL)),
                ('unliked', models.ManyToManyField(blank=True, related_name='unliked', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=models.SET(posts.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]