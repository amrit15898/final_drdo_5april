# Generated by Django 4.1.7 on 2023-02-23 11:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_appointment_organization_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='clearance_level',
            field=models.CharField(choices=[('red', 'red'), ('green', 'green'), ('yellow', 'yellow')], default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='tem_id',
            field=models.UUIDField(default=uuid.UUID('b0c5a7cd-96c7-44c2-bf0f-a454de92438d')),
        ),
    ]