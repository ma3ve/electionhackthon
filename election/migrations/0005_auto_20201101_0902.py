# Generated by Django 3.1.2 on 2020-11-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0004_auto_20201101_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='candidate'),
        ),
        migrations.AlterField(
            model_name='election',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='election'),
        ),
    ]