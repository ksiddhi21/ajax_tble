# Generated by Django 2.2.1 on 2019-09-21 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0015_auto_20190919_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_vendor_payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done')], default='Pending', max_length=20),
        ),
    ]
