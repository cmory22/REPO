# Generated by Django 3.0.4 on 2020-03-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_novinky_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novinky',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]