# Generated by Django 5.0.1 on 2024-01-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_description_alter_course_requirements_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]
