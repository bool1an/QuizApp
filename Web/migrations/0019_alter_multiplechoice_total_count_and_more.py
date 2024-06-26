# Generated by Django 5.0.2 on 2024-05-01 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0018_multiplechoice_total_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplechoice',
            name='total_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='multiplechoiceanswers',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='singlechoiceanswers',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='finished_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 1, 19, 39, 50, 602485)),
        ),
    ]
