# Generated by Django 2.2.4 on 2021-02-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hlist', '0019_auto_20201215_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mileage',
            name='year',
            field=models.IntegerField(default=2021),
        ),
    ]
