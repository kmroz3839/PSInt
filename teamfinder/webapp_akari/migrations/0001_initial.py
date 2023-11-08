# Generated by Django 4.2.7 on 2023-11-08 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dataConfigJson', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='UserSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playername', models.CharField(max_length=100)),
                ('playerurl', models.CharField(max_length=150)),
                ('data1', models.IntegerField(default=0)),
                ('data2', models.IntegerField(default=0)),
                ('data3', models.IntegerField(default=0)),
                ('data4', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp_akari.gameentry')),
            ],
        ),
    ]
