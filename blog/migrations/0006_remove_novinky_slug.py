# Generated by Django 3.0.4 on 2020-03-16 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_novinky_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novinky',
            name='slug',
        ),
    ]
