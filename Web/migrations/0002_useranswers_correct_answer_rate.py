# Generated by Django 5.0.2 on 2024-04-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswers',
            name='correct_answer_rate',
            field=models.FloatField(default=-1),
        ),
    ]
