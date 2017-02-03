from django.contrib import admin
from main.models import *


def update_profit(modeladmin, request, queryset):
    for i in queryset:
        i.conditionalProfit = i.prize - i.fine
        i.save()
update_profit.short_description = "Update profit"


def update_cp(modeladmin, request, queryset):
    ConditionalProfit.objects.all().delete()
    for i in EventList.objects.all():
        for j in ActionList.objects.all():
            CP = ConditionalProfit(action=j, event=i, probability=i.probability)
            CP.save()
            print(i, j, i.probability)
update_cp.short_description = "Update conditional profit table"


class EventListAdmin(admin.ModelAdmin):
    actions = [update_cp]
    list_display = ('event', 'probability')

admin.site.register(EventList, EventListAdmin)


class ActionListAdmin(admin.ModelAdmin):
    actions = [update_cp]
    list_display = ('action',)

admin.site.register(ActionList, ActionListAdmin)


class ConditionalProfitAdmin(admin.ModelAdmin):
    list_display = ('action', 'event', 'probability', 'prize', 'fine', 'conditionalProfit',)
    actions = [update_profit, update_cp]
    readonly_fields = ('action', 'event', 'probability', 'conditionalProfit')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



admin.site.register(ConditionalProfit, ConditionalProfitAdmin)




