# Generated by Django 4.1.3 on 2023-03-29 09:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0082_appointment_created_at_alter_appointment_tem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='tem_id',
            field=models.UUIDField(default=uuid.UUID('d0980b05-2c6f-4cbc-a273-0b2907a22519')),
        ),
    ]
