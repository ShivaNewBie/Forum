# Generated by Django 3.0 on 2022-01-30 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumpost', '0002_auto_20220130_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumpost',
            name='updated_on',
        ),
    ]
