# Generated by Django 3.2.9 on 2021-12-22 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0011_auto_20211220_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Sum',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
