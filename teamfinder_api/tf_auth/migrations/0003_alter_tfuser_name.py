# Generated by Django 4.2.7 on 2024-01-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tf_auth', '0002_remove_tfuser_username_tfuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfuser',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]