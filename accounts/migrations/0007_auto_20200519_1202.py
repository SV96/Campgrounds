# Generated by Django 3.0.6 on 2020-05-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200519_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(db_column='ITEM_IMAGE', upload_to='profile', verbose_name='IMAGE'),
        ),
    ]
