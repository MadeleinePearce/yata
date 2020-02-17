# Generated by Django 3.0.1 on 2020-02-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0004_target_targetinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='status_color',
            field=models.CharField(blank=True, default='last_action_relative', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='target',
            name='life_maximum',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='target',
            name='name',
            field=models.CharField(default='target_name', max_length=16),
        ),
    ]
