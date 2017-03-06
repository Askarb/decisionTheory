from django.contrib import admin
from arkansas.models import *


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
                year=j.year,
                CostBuild=i.CostBuild,
                costEx=i.costEx,
                cp=round(cp)
            )
            CP.save()
update_cp.short_description = "Update conditional profit table"


class EventListAdmin(admin.ModelAdmin):
    actions = [update_cp,]
    fields = ('event', 'probability')
    list_display = ('event', 'probability')


class ActionListAdmin(admin.ModelAdmin):
    # actions = [update_cp,]
    list_display = ('action', 'costBuild', 'costEx', 'year')


class ConditionalProfitAdmin(admin.ModelAdmin):
    actions = [update_cp,]
    list_display = ('action', 'event', 'probability', 'yearRevenue',
                    'ExpectRevenue', 'CostBuild', 'costEx', 'year', 'cp', 'EDP', 'ODT')
    fields = ('action', 'event', 'probability', 'yearRevenue',
                    'ExpectRevenue', 'CostBuild', 'costEx', 'year', 'cp','EDP', 'ODT')
    readonly_fields = ('action', 'event', 'probability', 'year', 'cp',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OPAdmin(admin.ModelAdmin):
    list_display = ('op',)

admin.site.register(ConditionalProfit, ConditionalProfitAdmin)
admin.site.register(ActionList, ActionListAdmin)
admin.site.register(EventList, EventListAdmin)
admin.site.register(MP, OPAdmin)

