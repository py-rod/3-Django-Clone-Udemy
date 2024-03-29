# Generated by Django 5.0.1 on 2024-01-22 07:39

import django.db.models.deletion
import index.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandsLogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(default='', upload_to=index.models.BrandsLogos.image_upload_to)),
            ],
            options={
                'verbose_name_plural': 'Upload Logos',
                'db_table': 'Brands_Logos',
            },
        ),
        migrations.CreateModel(
            name='ContentSection1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=254)),
                ('description', models.TextField(default='', max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Content Section 1',
            },
        ),
        migrations.CreateModel(
            name='SelectLogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_logo', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='index.brandslogos')),
            ],
            options={
                'verbose_name_plural': 'Select Logos',
                'db_table': 'Select_Logos',
            },
        ),
    ]
