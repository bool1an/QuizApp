# Generated by Django 5.0.2 on 2024-03-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0008_alter_useranswers_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswers',
            name='stage',
            field=models.IntegerField(default=0),
        ),
    ]
