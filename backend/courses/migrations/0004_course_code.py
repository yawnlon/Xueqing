# Generated by Django 2.2.1 on 2019-06-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_course_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(default='000000', max_length=10, verbose_name='code'),
        ),
    ]
