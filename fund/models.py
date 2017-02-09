from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ActionList(models.Model):
    action = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.action


class EventList(models.Model):
    class Meta:
        unique_together = ('event', 'probability')
    event = models.CharField(max_length=255)
    probability = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=1)

    def __str__(self):
        return self.event


class ConditionalProfit(models.Model):
    action = models.ForeignKey(ActionList)
    event = models.ForeignKey(EventList)
    probability = models.FloatField(default=0)
    conditionalProfit = models.FloatField(default=0, verbose_name=u'Прибль в %')
    profit = models.FloatField(default=0, )
    fine = models.FloatField(default=0, validators=[MinValueValidator(0),])


class InvestedCapital(models.Model):
    value = models.PositiveIntegerField()


