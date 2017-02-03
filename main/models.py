from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator


class ActionList(models.Model):
    action = models.CharField(max_length=255)

    def __str__(self):
        return self.action


class EventList(models.Model):
    event = models.CharField(max_length=255)
    probability = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=1)

    def __str__(self):
        return self.event


class ConditionalProfit(models.Model):
    action = models.ForeignKey(ActionList)
    event = models.ForeignKey(EventList)
    probability = models.FloatField(default=0)
    conditionalProfit = models.FloatField(default=0)
    prize = models.FloatField(default=0, validators=[MinValueValidator(0),], )
    fine = models.FloatField(default=0, validators=[MinValueValidator(0),])


@receiver(post_save, sender=EventList, dispatch_uid="update_stock_count")
def update_Event(sender, instance, **kwargs):
    print(instance, kwargs)
    #updateConditionalProfit()


@receiver(post_save, sender=ActionList, dispatch_uid="update_stock_count")
def update_Action(sender, instance, **kwargs):
    print(instance, kwargs)
    #updateConditionalProfit()
     # instance.product.stock -= instance.amount
     # instance.product.save()


# def updateConditionalProfit():
#     ConditionalProfit.objects.all().delete()
#     for i in EventList.objects.all():
#         for j in ActionList.objects.all():
#             CP = ConditionalProfit(action=j, event=i, probability=i.probability, conditionalProfit=0)
#             CP.save()
#             print(i,j, i.probability)
