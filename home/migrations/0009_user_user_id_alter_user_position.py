# Generated by Django 4.1.3 on 2022-11-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_appointment_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[('Director', 'Director'), ('Associate Director', 'Associate Director'), ('Tech Director', 'Tech Director'), ('GH/DH ', 'GH/DH'), ('Employee', 'Employee')], max_length=40),
        ),
    ]