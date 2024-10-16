# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings

from users.models import User as UserModel


def create_super_user(apps, schema_editor):
    User: UserModel = apps.get_model("users", "User")

    User.objects.create_superuser(
        id=settings.DJANGO_ADMIN_EMAIL,
        password=settings.DJANGO_ADMIN_PASSWORD,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_super_user),
    ]
