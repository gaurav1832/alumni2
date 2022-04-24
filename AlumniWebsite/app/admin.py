from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from app import models


class AlumnusInline(admin.StackedInline):
    model = models.Alumnus
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (AlumnusInline, )


class CircleAdmin(admin.ModelAdmin):
    model = models.Circle


class EventAdmin(admin.ModelAdmin):
    model = models.Event

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(models.Circle, CircleAdmin)
admin.site.register(models.Event, EventAdmin)