# Generated by Django 3.1.1 on 2020-10-02 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pickup_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 19, 41, 56, 350180)),
        ),
    ]