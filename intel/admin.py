from django.contrib import admin
from intel.models import *


def update_cp(modeladmin, request, queryset):
    ConditionalProfit.objects.all().delete()
    for i in EventList.objects.all():
        for j in ActionList.objects.all():
            if j.quality-i.percent >= 0:
                cp = (j.quality-i.percent)*j.prize/0.1
            else:
                cp = (j.quality - i.percent) * j.fine / 0.1

            CP = ConditionalProfit(
                action=j,
                event=i,
                probability=i.probability,
                quality=j.quality,
                percent=i.percent,
                conditionalProfit=round(cp)
            )
            CP.save()
update_cp.short_description = "Update conditional profit table"


class EventListAdmin(admin.ModelAdmin):
    actions = [update_cp,]
    fields = ('percent', 'probability')
    list_display = ('percent', 'probability')

admin.site.register(EventList, EventListAdmin)


class ActionListAdmin(admin.ModelAdmin):
    actions = [update_cp,]
    list_display = ('action', 'quality', 'prize', 'fine')

admin.site.register(ActionList, ActionListAdmin)


class ConditionalProfitAdmin(admin.ModelAdmin):
    list_display = ('action', 'event', 'percent', 'probability', 'quality', 'conditionalProfit',)
    fields = ('action', 'event', 'probability', 'quality', 'percent', 'conditionalProfit',)
    actions = [update_cp,]
    readonly_fields = ('action', 'event', 'probability', 'quality', 'percent', 'conditionalProfit',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ConditionalProfit, ConditionalProfitAdmin)
