# Generated by Django 4.2.3 on 2023-09-07 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создан'),
        ),
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активный'),
        ),
    ]