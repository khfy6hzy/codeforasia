# Generated by Django 3.0.4 on 2020-03-06 03:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200305_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='site',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 11, 27, 3, 670940), verbose_name='published date'),
        ),
    ]
