# Generated by Django 3.0.4 on 2020-03-16 19:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='novinky',
            options={'ordering': ['-vytvoreno']},
        ),
        migrations.AddField(
            model_name='novinky',
            name='vytvoreno',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
