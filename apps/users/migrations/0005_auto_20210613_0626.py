# Generated by Django 2.2.6 on 2021-06-13 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_auto_20210613_0445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='subcriber',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='user',
        ),
        migrations.AddField(
            model_name='follower',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='follow_client', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follower',
            name='sub',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='follow_sub', to='users.Profile'),
            preserve_default=False,
        ),
    ]