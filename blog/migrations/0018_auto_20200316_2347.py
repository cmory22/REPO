# Generated by Django 3.0.4 on 2020-03-16 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200316_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novinky',
            name='status',
            field=models.IntegerField(choices=[(1, 'Zahozeno'), (0, 'Publikováno')], default=0),
        ),
    ]
