# Generated by Django 3.1.2 on 2020-10-13 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactforms_app', '0006_auto_20201013_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='city',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='lname',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Last Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Phone Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='state',
            field=models.CharField(blank=True, default='', max_length=2, verbose_name='State'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='street_addr',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Street Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='years_participated',
            field=models.IntegerField(blank=True, default=0, verbose_name='Years in WF Baseball'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='zip_code',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Zip Code'),
            preserve_default=False,
        ),
    ]
