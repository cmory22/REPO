# Generated by Django 3.0.4 on 2020-03-16 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200316_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novinky',
            name='vytvoreno',
            field=models.DateField(auto_now_add=True),
        ),
    ]