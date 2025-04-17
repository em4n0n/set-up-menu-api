# Generated by Django 5.2 on 2025-04-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('no_of_guests', models.IntegerField()),
                ('bookingdate', models.DateTimeField()),
            ],
            options={
                'db_table': 'booking',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('inventory', models.IntegerField()),
            ],
            options={
                'db_table': 'menu',
            },
        ),
    ]
