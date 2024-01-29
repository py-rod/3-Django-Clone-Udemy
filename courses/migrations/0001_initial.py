# Generated by Django 5.0.1 on 2024-01-22 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300)),
                ('author', models.CharField(blank=True, default='', max_length=200)),
                ('will_learn', models.TextField(max_length=500)),
                ('requirements', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='SectionCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='VideoCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='videos')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.sectioncourse')),
            ],
        ),
    ]
