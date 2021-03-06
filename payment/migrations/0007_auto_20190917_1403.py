# Generated by Django 2.2.1 on 2019-09-17 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20190907_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='airticketsquatation',
            name='service_type',
            field=models.CharField(default='AirTicketService', max_length=70),
        ),
        migrations.AddField(
            model_name='entrancesquatation',
            name='service_type',
            field=models.CharField(default='EntrancesQuatationService', max_length=70),
        ),
        migrations.AddField(
            model_name='hotelquatation',
            name='service_type',
            field=models.CharField(default='HotelQuatationService', max_length=70),
        ),
        migrations.AddField(
            model_name='restaurantquatation',
            name='service_type',
            field=models.CharField(default='RestuarantQuatationService', max_length=70),
        ),
        migrations.AddField(
            model_name='sapsanquatation',
            name='service_type',
            field=models.CharField(default='SapSanQuatationService', max_length=70),
        ),
        migrations.AddField(
            model_name='visacostquatation',
            name='service_type',
            field=models.CharField(default='VisaCostService', max_length=70),
        ),
    ]
