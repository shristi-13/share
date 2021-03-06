# Generated by Django 2.0.7 on 2018-08-22 05:49

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=20, null=True)),
                ('version', models.CharField(max_length=5, null=True)),
                ('about', tinymce.models.HTMLField(blank=True, null=True, verbose_name='About')),
                ('note', models.TextField(blank=True, null=True)),
                ('modified_date_time', models.DateTimeField(auto_now=True)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('product_description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project', models.CharField(blank=True, max_length=20)),
                ('project_description', models.TextField(blank=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documentation.Product', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(blank=True, max_length=10, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='project',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='product', on_delete=django.db.models.deletion.CASCADE, to='documentation.Project'),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(to='documentation.Tags'),
        ),
    ]
