# Generated by Django 2.0.8 on 2019-03-27 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20190327_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum_plate',
            name='category_type',
        ),
        migrations.RemoveField(
            model_name='forum_plate',
            name='code',
        ),
        migrations.RemoveField(
            model_name='forum_plate',
            name='parent_category',
        ),
    ]
