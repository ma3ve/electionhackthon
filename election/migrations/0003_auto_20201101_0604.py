# Generated by Django 3.1.2 on 2020-11-01 06:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_auto_20201028_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='end',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='election',
            name='name',
            field=models.CharField(default='name', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='election',
            name='address',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
