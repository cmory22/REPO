# Generated by Django 3.0.4 on 2020-03-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_novinky_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='novinky',
            name='foto',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
