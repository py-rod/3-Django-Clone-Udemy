# Generated by Django 5.0.1 on 2024-01-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_description_alter_course_requirements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]