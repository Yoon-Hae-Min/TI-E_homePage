# Generated by Django 2.2.4 on 2020-12-04 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hlist', '0015_auto_20201130_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='mileage',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]
