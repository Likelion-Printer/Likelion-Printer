# Generated by Django 3.1.1 on 2020-10-02 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Printer_house',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=200)),
                ('phone_nubmer', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
