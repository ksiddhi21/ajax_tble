# Generated by Django 2.2.1 on 2019-10-02 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0025_auto_20191001_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupdescription',
            name='groupdescription_vtrefNo',
            field=models.CharField(max_length=264),
        ),
    ]