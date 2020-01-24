# Generated by Django 2.2.1 on 2019-09-26 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0018_vendor_vendor_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payment.Service')),
                ('Guide_Name', models.CharField(max_length=300)),
                ('Guide_Destination', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Guide',
                'verbose_name_plural': 'Guide',
            },
            bases=('payment.service',),
        ),
    ]
