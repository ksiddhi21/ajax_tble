# Generated by Django 2.2 on 2019-09-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0014_auto_20190919_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupdescription',
            name='groupdescription_traveling_date',
        ),
        migrations.AlterField(
            model_name='service',
            name='service_total_amount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
