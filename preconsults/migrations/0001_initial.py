# Generated by Django 3.1.4 on 2020-12-07 02:14

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='preconsult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=40)),
                ('age', models.CharField(max_length=3)),
                ('profession', models.CharField(max_length=50)),
                ('surgery', models.TextField(max_length=500)),
                ('expectancy', models.TextField(max_length=1000)),
                ('fear', models.TextField(max_length=1000)),
                ('recommendation', models.TextField(max_length=100)),
                ('rhinoplasty', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('creation_date', models.DateField(default=datetime.date.today)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]