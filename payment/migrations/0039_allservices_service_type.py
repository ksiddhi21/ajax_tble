# Generated by Django 2.2.1 on 2019-10-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0038_allservices'),
    ]

    operations = [
        migrations.AddField(
            model_name='allservices',
            name='service_type',
            field=models.CharField(default='All Services', max_length=920),
        ),
    ]
