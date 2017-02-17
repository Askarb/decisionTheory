from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ActionList(models.Model):
    action = models.CharField(max_length=255, unique=True)
    quality = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        verbose_name=u'Процент брака по контракту'
    )
    prize = models.FloatField(
        verbose_name=u'Премия',
        validators=[MinValueValidator(0), ],
        default=0
    )
    fine = models.FloatField(
        verbose_name=u'Штраф',
        validators=[MinValueValidator(0), ],
        default=0
    )

    def __str__(self):
        return self.action


class EventList(models.Model):
    class Meta:
        unique_together = ('percent', 'probability')

    event = models.CharField(max_length=255)
    percent = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        verbose_name=u'Процент брака по делу'
    )
    probability = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1)],
        default=1
    )

    def __str__(self):
        return self.event


class ConditionalProfit(models.Model):
    action = models.ForeignKey(ActionList)
    event = models.ForeignKey(EventList)
    probability = models.FloatField(default=0)
    quality = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        verbose_name=u'Процент брака по контракту'
    )
    percent = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        verbose_name=u'Процент брака по делу'
    )
    conditionalProfit = models.FloatField(default=0, verbose_name=u'Прибль в $')
