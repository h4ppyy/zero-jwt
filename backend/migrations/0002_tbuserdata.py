# Generated by Django 2.2.7 on 2019-11-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbUserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.CharField(max_length=255)),
                ('timestamp', models.CharField(max_length=255)),
                ('accleX', models.CharField(max_length=255)),
                ('accleY', models.CharField(max_length=255)),
                ('accleZ', models.CharField(max_length=255)),
                ('roll', models.CharField(max_length=255)),
                ('pitch', models.CharField(max_length=255)),
                ('azimuth', models.CharField(max_length=255)),
                ('gyroX', models.CharField(max_length=255)),
                ('gyroY', models.CharField(max_length=255)),
                ('gyroZ', models.CharField(max_length=255)),
                ('gpsLat', models.CharField(max_length=255)),
                ('gpsLon', models.CharField(max_length=255)),
                ('gpsAlt', models.CharField(max_length=255)),
                ('gpsAcc', models.CharField(max_length=255)),
                ('gpsTime', models.CharField(max_length=255)),
                ('NgpsLat', models.CharField(max_length=255)),
                ('NgpsLon', models.CharField(max_length=255)),
                ('NgpsAlt', models.CharField(max_length=255)),
                ('NgpsAcc', models.CharField(max_length=255)),
                ('NgpsTime', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_data',
            },
        ),
    ]
