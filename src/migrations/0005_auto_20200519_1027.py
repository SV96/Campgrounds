# Generated by Django 3.0.6 on 2020-05-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_auto_20200519_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campground',
            name='amount_type',
            field=models.CharField(choices=[('day', 'day'), ('week', 'week')], max_length=10),
        ),
    ]
