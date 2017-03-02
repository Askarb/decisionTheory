from django.contrib import admin
from engine.models import *


def update_cp(modeladmin, request, queryset):
    ConditionalProfit.objects.all().delete()
    for i in EventList.objects.all():
        for j in ActionList.objects.all():
            CP = ConditionalProfit(action=j, event=i, probability=i.probability)
            CP.save()
update_cp.short_description = "Update conditional profit table"


def update_profit(modeladmin, request, queryset):
    for i in queryset:
        i.cp = i.revenue - i.cost - i.expence
        i.save()
update_profit.short_description = "Update CP"


class EventListAdmin(admin.ModelAdmin):
    actions = [update_cp, update_profit]
    list_display = ('event', 'action', 'probability')


class ActionListAdmin(admin.ModelAdmin):
    actions = [update_cp, update_profit]
    list_display = ('action',)


class ConditionalProfitAdmin(admin.ModelAdmin):
    actions = [update_profit]
    list_display = ('action', 'event', 'probability', 'revenue', 'cost', 'expence', 'cp',)
    fields = ('action', 'event', 'probability', 'revenue', 'cost', 'expence',)
    readonly_fields = ('action', 'event', 'probability', 'cp' )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ConditionalProfit, ConditionalProfitAdmin)
admin.site.register(ActionList, ActionListAdmin)
admin.site.register(EventList, EventListAdmin)

