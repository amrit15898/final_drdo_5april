# Generated by Django 4.1.7 on 2023-03-06 07:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0074_appointment_transporation_requirement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='tem_id',
            field=models.UUIDField(default=uuid.UUID('437d1de7-2393-4e40-a72a-ebb5089e0cab')),
        ),
    ]
