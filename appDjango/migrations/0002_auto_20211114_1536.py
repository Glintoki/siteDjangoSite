# Generated by Django 3.2.9 on 2021-11-14 10:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouseworker',
            name='Worker_Address',
        ),
        migrations.AddField(
            model_name='warehouseworker',
            name='Worker_Login',
            field=models.CharField(default='some string', max_length=25),
        ),
        migrations.AddField(
            model_name='warehouseworker',
            name='Worker_Password',
            field=models.CharField(default='some string', max_length=25),
        ),
        migrations.AlterField(
            model_name='expenditureinvoice',
            name='Expend_Date',
            field=models.DateField(default=datetime.datetime(2021, 11, 14, 10, 36, 23, 844205, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_Expiration_Date',
            field=models.DateField(default=datetime.datetime(2021, 11, 14, 10, 36, 23, 842253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_Production_Date',
            field=models.DateField(default=datetime.datetime(2021, 11, 14, 10, 36, 23, 842253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='receiptinvoice',
            name='Receipt_Date',
            field=models.DateField(default=datetime.datetime(2021, 11, 14, 10, 36, 23, 841276, tzinfo=utc)),
        ),
    ]
