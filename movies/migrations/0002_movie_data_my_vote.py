# Generated by Django 3.2.7 on 2021-11-25 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_data',
            name='my_vote',
            field=models.IntegerField(null=True),
        ),
    ]
