# Generated by Django 5.0.2 on 2024-04-30 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0011_test_correct_rate_all_alter_test_published_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='correct_rate_all',
        ),
        migrations.AddField(
            model_name='useranswers',
            name='correct_answers',
            field=models.FloatField(default=-1),
        ),
        migrations.AlterField(
            model_name='test',
            name='published_at',
            field=models.DateField(default=datetime.datetime(2024, 4, 30, 15, 14, 25, 608388, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='finished_at',
            field=models.DateField(default=datetime.datetime(2024, 4, 30, 15, 14, 25, 611120, tzinfo=datetime.timezone.utc)),
        ),
    ]