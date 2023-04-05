# Generated by Django 4.1.7 on 2023-03-01 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0061_alter_appointment_tem_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='posted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postted_byy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointment',
            name='pvt_request',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='tem_id',
            field=models.UUIDField(default=uuid.UUID('f579f578-5f5d-4e35-a15b-5ab78370ad62')),
        ),
    ]
