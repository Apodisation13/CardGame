# Generated by Django 3.2.8 on 2022-08-24 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_create_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
    ]
