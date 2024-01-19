# Generated by Django 5.0.1 on 2024-01-19 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_is_social_account_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='departament',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='description',
        ),
        migrations.AddField(
            model_name='customuser',
            name='biografy',
            field=models.TextField(blank=True, default='', max_length=600),
        ),
        migrations.AddField(
            model_name='customuser',
            name='facebook_link',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AddField(
            model_name='customuser',
            name='instructor_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='customuser',
            name='language',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='customuser',
            name='linkin_link',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AddField(
            model_name='customuser',
            name='paypal_account',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AddField(
            model_name='customuser',
            name='twitter_link',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AddField(
            model_name='customuser',
            name='web_site_link',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AddField(
            model_name='customuser',
            name='youtube_link',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]
