# Generated by Django 2.2.1 on 2019-09-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0023_auto_20190926_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='service_type',
            field=models.CharField(default='Guide Service', max_length=70),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_type',
            field=models.CharField(choices=[('Air Ticket Service', 'Air Ticket Service'), ('Visa Cost Service', 'Visa Cost Service'), ('Hotel Quatation Service', 'Hotel Quatation Service'), ('Restuarant Quatation Service', 'Restuarant Quatation Service'), ('Entrances Quatation Service', 'Entrances Quatation Service'), ('SapSan Quatation Service', 'SapSan Quatation Service'), ('Guide Service', 'Guide Service')], default='Air Ticket Service', max_length=264),
        ),
    ]
