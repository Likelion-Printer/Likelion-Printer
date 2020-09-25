# Generated by Django 3.0.8 on 2020-09-25 07:17

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('confirmations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_canceled', models.BooleanField(default=False)),
                ('is_in_process', models.BooleanField(default=True)),
                ('order_time', models.DateTimeField(auto_now=True)),
                ('pickup_time', models.DateTimeField(default=datetime.datetime(2020, 9, 25, 17, 17, 33, 492401))),
                ('status', models.CharField(choices=[('confirmed', '주문확인'), ('complete', '인쇄완료'), ('pending', '주문대기')], default='pending', max_length=200)),
                ('options_color', models.CharField(choices=[('black', '흑백'), ('color', '칼라')], default='black', max_length=200)),
                ('options_print', models.CharField(choices=[('single', '단면'), ('double', '양면')], default='double', max_length=200)),
                ('options_pages', models.CharField(choices=[('four', '4개'), ('two', '2개'), ('one', '1개')], default='four', max_length=200)),
                ('number_of_pages', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(70), django.core.validators.MinValueValidator(1)])),
                ('options_directions', models.CharField(choices=[('horizontal', '가로'), ('vertical', '세로')], default='vertical', max_length=200)),
                ('options_flip', models.CharField(choices=[('horizontal', '옆으로 넘김'), ('vertical', '위로 넘김')], default='horizontal', max_length=200)),
                ('comments', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('printer_house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='confirmations.Printer_house')),
            ],
        ),
    ]
