# Generated by Django 2.2.1 on 2019-06-22 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudyCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='code')),
                ('introduction', models.CharField(blank=True, default='', max_length=1000, verbose_name='introduction')),
                ('class_free', models.BooleanField(default=False, verbose_name='class_free')),
                ('class_general', models.BooleanField(default=False, verbose_name='class_general')),
                ('class_vip', models.BooleanField(default=False, verbose_name='class_vip')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='add_time')),
            ],
        ),
    ]