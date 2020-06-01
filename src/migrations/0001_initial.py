# Generated by Django 3.0.6 on 2020-05-19 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=100)),
                ('amount_type', models.CharField(choices=[('day', 'day'), ('week', 'week')], max_length=10)),
                ('amount', models.IntegerField(default=0)),
                ('created_date_post', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('location', models.CharField(blank=True, max_length=25, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date_comment', models.DateField(default=django.utils.timezone.now)),
                ('comment_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentor', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='src.Campground')),
            ],
        ),
        migrations.CreateModel(
            name='BookCamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact', models.IntegerField(blank=True, default=0, null=True)),
                ('time', models.CharField(blank=True, max_length=25, null=True)),
                ('camp_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reserve', to='src.Campground')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]