# Generated by Django 3.2.9 on 2021-12-22 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0012_alter_product_product_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Sum',
            field=models.IntegerField(default=0),
        ),
    ]
