# Generated by Django 3.2.9 on 2021-11-21 21:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211121_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_genre',
            name='like_genres',
            field=models.ManyToManyField(blank=True, related_name='likinggenres', to=settings.AUTH_USER_MODEL),
        ),
    ]
