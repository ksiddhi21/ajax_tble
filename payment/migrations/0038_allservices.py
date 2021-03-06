# Generated by Django 2.2.1 on 2019-10-16 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0037_auto_20191016_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllServices',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payment.Service')),
                ('allservices_airticket', models.BooleanField(default=False)),
                ('allservices_visacost', models.BooleanField(default=False)),
                ('allservices_hotel', models.BooleanField(default=False)),
                ('allservices_restaurant', models.BooleanField(default=False)),
                ('allservices_entrances', models.BooleanField(default=False)),
                ('allservices_sapsan', models.BooleanField(default=False)),
                ('allservices_guide', models.BooleanField(default=False)),
                ('allservices_transport', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'AllServices',
                'verbose_name_plural': 'AllServices',
            },
            bases=('payment.service',),
        ),
    ]
