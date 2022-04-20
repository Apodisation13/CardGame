# Generated by Django 3.2.8 on 2022-04-20 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_ability_enemyleaderability_enemypassiveability_move_passiveability_type'),
        ('enemies', '0004_rename_passive_ability_id_enemy_passive_ability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enemy',
            name='move',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='enemies', to='core.move'),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='passive_ability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='enemies', to='core.enemypassiveability'),
        ),
        migrations.AlterField(
            model_name='enemyleader',
            name='ability',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='enemy_leaders', to='core.enemyleaderability'),
        ),
        migrations.DeleteModel(
            name='EnemyLeaderAbility',
        ),
        migrations.DeleteModel(
            name='EnemyPassiveAbility',
        ),
        migrations.DeleteModel(
            name='Move',
        ),
    ]
