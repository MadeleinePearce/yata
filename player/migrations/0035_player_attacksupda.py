# Generated by Django 3.0.1 on 2020-02-16 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0034_auto_20200130_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='attacksUpda',
            field=models.IntegerField(default=0),
        ),
    ]
