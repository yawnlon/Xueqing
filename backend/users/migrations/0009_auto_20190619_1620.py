# Generated by Django 2.2.1 on 2019-06-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_smscode_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smscode',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='添加时间'),
        ),
    ]
