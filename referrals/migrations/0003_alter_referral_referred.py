# Generated by Django 5.1.2 on 2024-10-14 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("referrals", "0002_alter_referral_referred"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="referral",
            name="referred",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.SET,
                related_name="referral",
                to="users.user",
            ),
        ),
    ]
