# Generated by Django 3.1.2 on 2020-10-22 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactforms_app', '0011_auto_20201013_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email Address'),
        ),
    ]
