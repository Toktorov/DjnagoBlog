# Generated by Django 2.2.6 on 2021-06-13 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='subcriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_subcriber', to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_user', to=settings.AUTH_USER_MODEL),
        ),
    ]