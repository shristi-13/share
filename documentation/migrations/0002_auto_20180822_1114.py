# Generated by Django 2.0.7 on 2018-08-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='author',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]