# Generated by Django 2.0.7 on 2018-08-30 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0005_auto_20180828_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documentation.Product'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='tags',
            name='tag_name',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
