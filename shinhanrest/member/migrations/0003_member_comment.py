# Generated by Django 4.1.5 on 2023-01-19 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_member_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='comment',
            field=models.CharField(default='', max_length=50, verbose_name='댓글'),
            preserve_default=False,
        ),
    ]