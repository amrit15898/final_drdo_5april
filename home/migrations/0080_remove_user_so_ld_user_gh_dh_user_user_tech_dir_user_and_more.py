# Generated by Django 4.1.3 on 2023-03-29 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0079_appointment_final_status_alter_appointment_tem_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='so_ld',
        ),
        migrations.AddField(
            model_name='user',
            name='gh_dh_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gh_dhh', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='tech_dir_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_dirr', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='tem_id',
            field=models.UUIDField(default=uuid.UUID('6471c8ed-6b02-4154-95d9-cf3d3d0d6106')),
        ),
    ]
