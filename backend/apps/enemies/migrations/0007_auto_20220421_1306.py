# Generated by Django 3.2.8 on 2022-04-21 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enemies', '0006_auto_20220420_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='unlocked',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_level', to='enemies.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_level', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
