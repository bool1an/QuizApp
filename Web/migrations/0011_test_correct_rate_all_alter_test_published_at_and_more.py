# Generated by Django 5.0.2 on 2024-04-30 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0010_alter_test_published_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='correct_rate_all',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='published_at',
            field=models.DateField(default=datetime.datetime(2024, 4, 30, 12, 32, 32, 610674, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='finished_at',
            field=models.DateField(default=datetime.datetime(2024, 4, 30, 12, 32, 32, 620978, tzinfo=datetime.timezone.utc)),
        ),
    ]