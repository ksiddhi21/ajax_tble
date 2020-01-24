# Generated by Django 2.2.7 on 2019-11-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0044_visitingcardcompanydata_visitingcardcompanydata_convert_to_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupdescription',
            name='groupdescription_number_of_adult_passengers',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='groupdescription',
            name='groupdescription_number_of_adult_quote_per_head',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='groupdescription',
            name='groupdescription_number_of_child_passengers',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='groupdescription',
            name='groupdescription_number_of_child_quote_per_head',
            field=models.FloatField(default=0.0),
        ),
    ]
