from django.contrib import admin

from list.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
