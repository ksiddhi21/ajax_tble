# Generated by Django 2.2.1 on 2019-09-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0021_auto_20190926_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visacostquatation',
            name='visacost_visa_letter_cost',
            field=models.IntegerField(default=10),
        ),
    ]
