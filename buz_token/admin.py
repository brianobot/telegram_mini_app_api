from django.contrib import admin

from buz_token.models import BuzToken
from buz_token.models import Task
from buz_token.models import UserTask


@admin.register(BuzToken)
class BuzTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'channel', 'created_at']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['description', 'max_users', 'reward', 'can_reward_user', 'user_rewarded', 'tokens_awarded']


@admin.register(UserTask)
class UserTaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'task', 'reward', 'created_at']