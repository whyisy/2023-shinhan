# Generated by Django 4.1.5 on 2023-01-19 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_member_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='comment',
        ),
    ]
