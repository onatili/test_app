# Generated by Django 4.2.6 on 2023-10-25 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_test_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 27, 6, 21, 21, 9621, tzinfo=datetime.timezone.utc), verbose_name='tugash sanasi'),
        ),
    ]
