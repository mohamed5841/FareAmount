# Generated by Django 5.0.6 on 2024-05-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_latitude', models.FloatField()),
                ('pickup_longitude', models.FloatField()),
                ('dropoff_latitude', models.FloatField()),
                ('dropoff_longitude', models.FloatField()),
                ('displacement', models.FloatField()),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bearing', models.DecimalField(decimal_places=2, max_digits=6)),
                ('nyc_dist', models.DecimalField(decimal_places=2, max_digits=10)),
                ('day', models.IntegerField()),
                ('hour', models.IntegerField()),
            ],
        ),
    ]