# Generated by Django 4.1.2 on 2022-11-28 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.department'),
        ),
    ]
