# Generated by Django 3.0.4 on 2020-03-06 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200306_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('demographics', models.TextField(default='Write here')),
                ('channels', models.TextField(default='Write here')),
                ('impact', models.TextField(default='Write here')),
                ('activities', models.TextField(default='Write here')),
                ('innovative', models.TextField(default='Write here')),
                ('challenges', models.TextField(default='Write here')),
            ],
        ),
        migrations.AlterField(
            model_name='form',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 13, 47, 44, 103587), verbose_name='published date'),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 13, 47, 44, 104614), verbose_name='Birth data'),
        ),
        migrations.AlterField(
            model_name='site',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 13, 47, 44, 103587), verbose_name='published date'),
        ),
    ]
