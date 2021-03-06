# Generated by Django 3.2.8 on 2021-10-26 10:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_Sum', models.IntegerField(default=0)),
                ('Order_Id_Product', models.IntegerField(default=0)),
                ('Order_Name_Store', models.CharField(max_length=25)),
                ('Order_Address', models.CharField(max_length=100)),
                ('Order_Surname', models.CharField(max_length=50)),
                ('Order_Name', models.CharField(max_length=50)),
                ('Order_Patronymic', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Provider_Surname', models.CharField(max_length=50)),
                ('Provider_Name', models.CharField(max_length=50)),
                ('Provider_Patronymic', models.CharField(max_length=50)),
                ('Provide_Number', models.CharField(max_length=11)),
                ('Provide_Address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Worker_Surname', models.CharField(max_length=50)),
                ('Worker_Name', models.CharField(max_length=50)),
                ('Worker_Patronymic', models.CharField(max_length=50)),
                ('Worker_Number', models.CharField(max_length=11)),
                ('Worker_Address', models.CharField(max_length=100)),
                ('Worker_Position', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receipt_Date', models.DateField(default=datetime.datetime(2021, 10, 26, 10, 8, 54, 256970, tzinfo=utc))),
                ('Receipt_Sum', models.IntegerField(default=0)),
                ('Receipt_Price', models.IntegerField(default=0)),
                ('Receipt_Id_Product', models.IntegerField(default=0)),
                ('Receipt_Id_Provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDjango.provider')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=25)),
                ('Product_Price', models.IntegerField(default=0)),
                ('Product_Sum', models.IntegerField(default=0)),
                ('Product_Expiration_Date', models.DateField(default=datetime.datetime(2021, 10, 26, 10, 8, 54, 257988, tzinfo=utc))),
                ('Product_Production_Date', models.DateField(default=datetime.datetime(2021, 10, 26, 10, 8, 54, 257988, tzinfo=utc))),
                ('Product_Arrival_ID', models.ManyToManyField(to='appDjango.Arrival')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenditureInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Expend_Date', models.DateField(default=datetime.datetime(2021, 10, 26, 10, 8, 54, 259961, tzinfo=utc))),
                ('Expend_Price', models.IntegerField(default=0)),
                ('Expend_ID_Product', models.IntegerField(default=0)),
                ('Expend_Sum', models.IntegerField(default=0)),
                ('Expend_Id_Consumption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDjango.consumption')),
            ],
        ),
        migrations.AddField(
            model_name='consumption',
            name='Consumption_Id_Order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDjango.order'),
        ),
        migrations.AddField(
            model_name='consumption',
            name='Consumption_Id_Worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDjango.warehouseworker'),
        ),
        migrations.AddField(
            model_name='consumption',
            name='Consumption_Product_ID',
            field=models.ManyToManyField(to='appDjango.Product'),
        ),
        migrations.AddField(
            model_name='arrival',
            name='ID_Receipt_Invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDjango.receiptinvoice'),
        ),
        migrations.AddField(
            model_name='arrival',
            name='ID_Worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDjango.warehouseworker'),
        ),
    ]
