# Generated by Django 3.2.8 on 2022-04-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='resource',
            new_name='scraps',
        ),
        migrations.AddField(
            model_name='customuser',
            name='big_kegs',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='chests',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='kegs',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='customuser',
            name='wood',
            field=models.IntegerField(default=1000),
        ),
    ]