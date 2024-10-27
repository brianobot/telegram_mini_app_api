# Generated by Django 5.1.2 on 2024-10-27 21:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("referrals", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name="referral",
            index=models.Index(
                fields=["referrer"], name="referrals_r_referre_18a7a2_idx"
            ),
        ),
    ]