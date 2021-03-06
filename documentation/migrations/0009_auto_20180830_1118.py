# Generated by Django 2.0.7 on 2018-08-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0008_auto_20180830_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='tag_name',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
