# Generated by Django 2.2.1 on 2019-09-23 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0016_service_service_vendor_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_id',
            field=models.ForeignKey(default='11', on_delete=django.db.models.deletion.CASCADE, to='payment.Groupdescription'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_vendor_id',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='payment.Vendor'),
        ),
    ]