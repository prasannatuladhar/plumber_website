# Generated by Django 3.0.6 on 2020-05-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=100)),
                ('your_phone', models.IntegerField(max_length=15)),
                ('your_email', models.EmailField(max_length=150)),
                ('your_address', models.CharField(max_length=100)),
                ('your_time', models.DateField()),
                ('your_date', models.TimeField()),
                ('your_message', models.CharField(max_length=200)),
            ],
        ),
    ]
