# Generated by Django 4.1.7 on 2023-02-27 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_alter_appointment_tem_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='so_ld',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='tem_id',
            field=models.UUIDField(default=uuid.UUID('78556426-e2ee-4e0b-a917-4719e73bca5e')),
        ),
    ]
