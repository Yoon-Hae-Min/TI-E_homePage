# Generated by Django 2.2.4 on 2020-11-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0009_auto_20201029_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='uploaddate',
            field=models.DateField(auto_now_add=True),
        ),
    ]