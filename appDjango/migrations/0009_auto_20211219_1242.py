# Generated by Django 3.2.9 on 2021-12-19 07:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0008_auto_20211211_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='anons',
            name='Anons_ExpirationDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='receiptinvoice',
            name='Receipt_Date',
            field=models.DateField(default=datetime.datetime(2021, 12, 19, 7, 42, 27, 24753, tzinfo=utc)),
        ),
    ]
