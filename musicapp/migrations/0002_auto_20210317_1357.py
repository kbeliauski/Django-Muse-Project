# Generated by Django 3.1.7 on 2021-03-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
