# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from buz_token.models import Task as TaskModel

FUNC_DECLARATION_STR = "def func(user):"


TASK_DATA = [
    {
        "id": "1",
        "description": "Follow Us on X",
        "max_users": 150_000,
        "action": "do",
        "reward": 4900,
        "metadata": {
            "code": f"{FUNC_DECLARATION_STR} return True"
        }
    },
    {
        "id": "2",
        "description": "Be one of the first 4,900 players to refer 7 users",
        "max_users": 4900,
        "action": "claim",
        "reward": 98_000,
        "metadata": {
            "code": f"{FUNC_DECLARATION_STR} return user.referrals >= 7"
        }
    },
    {
        "id": "3",
        "description": "Be one of the first 7,000 players to earn 28,000 BUZ from quiz",
        "max_users": 350_000,
        "action": "claim",
        "reward": 7000,
        "metadata": {
            "code": f"{FUNC_DECLARATION_STR} from buz_token.models import BuzToken;return BuzToken.objects.filter(channel='games', user=user).aggregate(total=Sum('amount')).get('total', 0) or 0 >= 28_000"
        }
    },
    {
        "id": "4",
        "description": "Be one of the first 39,200 users to reach 56,700 BUZ",
        "max_users": 39_200,
        "action": "claim",
        "reward": 49_000,
        "metadata": {
            "code": f"{FUNC_DECLARATION_STR} from buz_token.models import BuzToken;return BuzToken.objects.filter(user=user).aggregate(total=Sum('amount')).get('total', 0) or 0 >= 56_700"
        }
    },
    {
        "id": "5",
        "description": "Be one of the first 4,200 users to reach 147,000 BUZ",
        "max_users": 1_190_000,
        "action": "claim",
        "reward": 4200,
        "metadata": {
            "code": f"{FUNC_DECLARATION_STR} from buz_token.models import BuzToken;return BuzToken.objects.filter(user=user).aggregate(total=Sum('amount')).get('total', 0) or 0 >= 147_000"
        }
    },
]


def create_tasks_data(apps, schema_editor):
    Task: TaskModel = apps.get_model("buz_token", "Task")

    for data in TASK_DATA:
        Task.objects.create(
            id=data.get("id"),
            action=data.get("action"),
            description=data.get('description'),
            max_users=data.get("max_users"),
            reward=data.get('reward'),
            metadata=data.get("metadata"),
        )



class Migration(migrations.Migration):
    dependencies = [
        ("buz_token", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_tasks_data),
    ]
