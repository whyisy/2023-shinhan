# Generated by Django 4.1.5 on 2023-01-19 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comment',
            field=models.CharField(default='', max_length=50, verbose_name='댓글'),
            preserve_default=False,
        ),
    ]
