# Generated by Django 2.2.1 on 2019-10-10 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0030_groupdescription_group_description_service_calculation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='visacostquatation',
            name='visacost_service_cost',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
