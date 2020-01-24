# Generated by Django 2.2.1 on 2019-10-24 04:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0040_auto_20191016_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitingCardAgencyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitingcardagencydata_agency_name', models.CharField(max_length=920)),
                ('visitingcardagencydata_agent_name', models.CharField(max_length=920)),
                ('visitingcardagencydata_agent_designation', models.CharField(max_length=920)),
                ('visitingcardagencydata_agency_address', models.CharField(max_length=920)),
                ('visitingcardagencydata_agency_city', models.CharField(max_length=920)),
                ('visitingcardagencydata_tel_numbers', models.CharField(max_length=920)),
                ('visitingcardagencydata_mobile_numbers', models.CharField(max_length=920)),
                ('visitingcardagencydata_email_address', models.CharField(max_length=920)),
                ('visitingcardagencydata_agency_website', models.CharField(max_length=920)),
                ('visitingcardagencydata_date_of_entry', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Agency Data',
                'verbose_name_plural': 'VisitingCardAgencyData',
            },
        ),
    ]
