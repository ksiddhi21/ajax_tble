# Generated by Django 2.2 on 2019-09-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupdescription',
            name='groupdescription_amount',
            field=models.IntegerField(default=0),
        ),
    ]