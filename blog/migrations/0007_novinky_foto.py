# Generated by Django 3.0.4 on 2020-03-16 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_novinky_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='novinky',
            name='foto',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
