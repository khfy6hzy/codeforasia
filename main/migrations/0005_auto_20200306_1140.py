# Generated by Django 3.0.4 on 2020-03-06 03:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200306_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 11, 40, 20, 816338), verbose_name='published date'),
        ),
    ]
