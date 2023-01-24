from django.contrib import admin
import datetime

from .models import (
    AdvUser,
    SuperRubric,
    SubRubric,
    Bb,
    AdditionalImage
)
from .forms import (
    SubRubricForm
)
from .utilities import send_activation_notification


# Register your models here.
def send_activation_notifications(modeladmin, request, queryset):
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
    modeladmin.message_user(request, 'Письма с требования отправлены')
    send_activation_notifications.short_description = 'Отправка писем с требованием активации'


class NonactivatedFilter(admin.SimpleListFilter):
    title = 'Прошли активацию?'
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Прошли'),
            ('threedays', 'Не прошли более 3-х дней'),
            ('week', 'Не прошли более недели')
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(
                is_active=True,
                is_activated=True
            )
        elif val == 'threedays':
            three_day_ago_date = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(
                is_active=False,
                is_activated=False,
                date_joined__date__lt=three_day_ago_date
            )
        elif val == 'week':
            week_ago_date = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(
                is_active=False,
                is_activated=False,
                date_joined__date__lt=week_ago_date
            )


class AdvUserAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'is_activated',
        'date_joined'
    )
    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name'
    )
    list_filter = (
        NonactivatedFilter,
    )
    fields = (
        ('username', 'email'),
        ('first_name', 'last_name'),
        ('is_staff', 'is_superuser'),
        ('groups',),
        ('user_permissions',),
        ('last_login', 'date_joined')
    )
    readonly_fields = (
        'last_login',
        'date_joined'
    )
    actions = (
        'send_activation_notifications',
    )


class SubRubricInline(admin.TabularInline):
    model = SubRubric


class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)


class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


class BbAdmin(admin.ModelAdmin):
    list_display = (
        'rubric',
        'title',
        'content',
        'author',
        'created_at'
    )
    fields = (
        ('rubric', 'author'),
        'title',
        'content',
        'price',
        'contacts',
        'image',
        'is_active'
    )
    inlines = (AdditionalImageInline,)


admin.site.register(AdvUser, AdvUserAdmin)
admin.site.register(SuperRubric, SuperRubricAdmin)
admin.site.register(SubRubric, SubRubricAdmin)
admin.site.register(Bb, BbAdmin)
