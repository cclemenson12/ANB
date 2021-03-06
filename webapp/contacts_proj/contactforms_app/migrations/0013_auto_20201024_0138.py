# Generated by Django 3.1.2 on 2020-10-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactforms_app', '0012_auto_20201022_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='comm_pref',
            field=models.CharField(blank=True, choices=[('E', 'Email'), ('M', 'Mail'), ('P', 'Phone'), ('T', 'Text Messages')], default='email', help_text='Choose the method you would prefer West Fargo Baseball use to contact you. Note: West Fargo Baseball may use email as primary for some communications', max_length=1, verbose_name='Communications Preference'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='duplicate',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='last_emailed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='news_events',
            field=models.BooleanField(blank=True, default=True, help_text='Check if you would like to get general news about West Fargo Baseball', verbose_name='Subscribe to West Fargo Baseball News'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='project_updates',
            field=models.BooleanField(blank=True, default=True, help_text='Check if you would like to get updates about West Fargo Baseball projects', verbose_name='Subscribe to Project Updates'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='unsubscribe',
            field=models.BooleanField(blank=True, default=False, help_text='Check if you wish to unsubscribe from all communications from West Fargo Baseball', verbose_name='Unsubscribe to all Communications'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='web_updated',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='years_participated',
            field=models.IntegerField(blank=True, default='0', verbose_name='Years in WF Baseball'),
            preserve_default=False,
        ),
    ]
