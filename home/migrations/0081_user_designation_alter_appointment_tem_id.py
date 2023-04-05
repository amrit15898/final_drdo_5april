# Generated by Django 4.1.3 on 2023-03-29 07:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0080_remove_user_so_ld_user_gh_dh_user_user_tech_dir_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='designation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='tem_id',
            field=models.UUIDField(default=uuid.UUID('eee5bba6-5633-450e-b99a-8935510d040e')),
        ),
    ]
