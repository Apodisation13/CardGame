# Generated by Django 3.2.8 on 2022-10-22 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enemies', '0007_auto_20221022_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='levels',
        ),
        migrations.DeleteModel(
            name='LevelSeason',
        ),
    ]