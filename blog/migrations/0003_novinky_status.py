# Generated by Django 3.0.4 on 2020-03-16 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200316_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='novinky',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]
