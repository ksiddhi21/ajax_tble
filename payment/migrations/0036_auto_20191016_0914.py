# Generated by Django 2.2.1 on 2019-10-16 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0035_auto_20191014_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_company_name',
            field=models.CharField(default='', max_length=920),
        ),
        migrations.AddField(
            model_name='client',
            name='client_website',
            field=models.CharField(default='', max_length=920),
        ),
    ]
