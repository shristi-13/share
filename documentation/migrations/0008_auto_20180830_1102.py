# Generated by Django 2.0.7 on 2018-08-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0007_auto_20180830_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
