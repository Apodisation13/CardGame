# Generated by Django 3.2.8 on 2022-04-02 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enemies', '0002_enemypassiveability'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy',
            name='passive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='enemy',
            name='passive_ability_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='enemies', to='enemies.enemypassiveability'),
        ),
        migrations.AddField(
            model_name='enemy',
            name='passive_damage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enemy',
            name='passive_heal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enemy',
            name='passive_heal_leader',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enemy',
            name='passive_increase_damage',
            field=models.IntegerField(default=0),
        ),
    ]