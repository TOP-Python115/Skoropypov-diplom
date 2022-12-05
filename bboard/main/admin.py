from django.contrib import admin
import datetime

from .models import AdvUser
from .utilities import send_activation_notification


# Register your models here.
def send_activation_notifications(modeladmin, request, queryset):
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
    modeladmin.message_user(request, 'Письма с требования отправлены')
    send_activation_notifications.short_description = 'Отправка писем с требованием активации'


