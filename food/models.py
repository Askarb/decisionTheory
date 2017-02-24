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
    action = models.ForeignKey(ActionList)

    probability = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=1)

    def __str__(self):
        return self.event


class ConditionalProfit(models.Model):
    action = models.ForeignKey(ActionList)
    event = models.ForeignKey(EventList)
    probability = models.FloatField(default=0)
    cp = models.FloatField(default=0,)
    revenue = models.FloatField(default=0,)
    cost = models.FloatField(default=0, )