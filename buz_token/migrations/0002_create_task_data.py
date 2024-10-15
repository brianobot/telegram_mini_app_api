# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from buz_token.models import Task as TaskModel


TASK_DATA = [
    {
        "description": "Follow Us on X",
        "max_users": 150_000,
        "reward": 4900,
    },
    {
        "description": "Be one of the first 4,900 players to refer 7 users",
        "max_users": 4900,
        "reward": 98_000,
    },
    {
        "description": "Be one of the first 7,000 players to earn 28,000 BUZ from quiz",
        "max_users": 350_000,
        "reward": 7000,
    },
    {
        "description": "Be one of the first 39,200 users to reach 56,700 BUZ",
        "max_users": 39_200,
        "reward": 49_000,
    },
    {
        "description": "Be one of the first 4,200 users to reach 147,000 BUZ",
        "max_users": 1_190_000,
        "reward": 4200,
    },
]


def create_tasks_data(apps, schema_editor):
    Task: TaskModel = apps.get_model("buz_token", "Task")

    for data in TASK_DATA:
        Task.objects.create(
            description=data.get('description'),
            max_users=data.get("max_users"),
            reward=data.get('reward'),
        )



class Migration(migrations.Migration):
    dependencies = [
        ("buz_token", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_tasks_data),
    ]
