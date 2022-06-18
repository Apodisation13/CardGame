# Generated by Django 3.2.8 on 2022-04-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enemies', '0001_initial'),
        ('cards', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cards',
            field=models.ManyToManyField(related_name='user_cards', through='cards.UserCard', to='cards.Card'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='decks',
            field=models.ManyToManyField(related_name='user_decks', through='cards.UserDeck', to='cards.Deck'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='leaders',
            field=models.ManyToManyField(related_name='user_leaders', through='cards.UserLeader', to='cards.Leader'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='levels',
            field=models.ManyToManyField(related_name='user_levels', through='enemies.UserLevel', to='enemies.Level'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]