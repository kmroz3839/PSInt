# Generated by Django 4.2.6 on 2023-11-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp_akari', '0002_gameentry_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubmission',
            name='submissiondate',
            field=models.DateTimeField(default='2000-06-06'),
        ),
    ]