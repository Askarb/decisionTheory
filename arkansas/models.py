from django.db import models
from arkansas.core import year
from django.core.validators import MaxValueValidator, MinValueValidator


class ActionList(models.Model):
    action = models.CharField(max_length=255, unique=True)
    costEx = models.FloatField(
        validators=[MinValueValidator(0),],
        default=0,
        verbose_name=u'Затраты на расширения'
    )
    costBuild = models.FloatField(
        verbose_name=u'Затраты на строительство',
        validators=[MinValueValidator(0), ],
        default=0
    )
    year = models.PositiveIntegerField(
        verbose_name=u'Количество лет до расширения!',
        validators=[MinValueValidator(0), MaxValueValidator(year()) ],
        default=0
    )

    def __str__(self):
        return self.action


class EventList(models.Model):
    class Meta:
        unique_together = ('event', 'probability')

    event = models.CharField(max_length=255)
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
    yearRevenue = models.FloatField(
        validators=[MinValueValidator(0),],
        default=0,
        verbose_name=u'Ежегодный доход до расширения'
    )
    ExpectRevenue = models.FloatField(
        validators=[MinValueValidator(0),],
        default=0,
        verbose_name=u'Ожидаемый доход в течении года'
    )
    CostBuild = models.FloatField(
        validators=[MinValueValidator(0),],
        default=0,
        verbose_name=u'Затраты на строительство'
    )
    year = models.FloatField(
        validators=[MinValueValidator(0),],
        default=0,
        verbose_name=u'Период до расширения')

    costEx = models.FloatField(
        validators=[MinValueValidator(0),],
        default=0,
        verbose_name=u'Затраты на расширения'
    )
    EDP = models.FloatField(
        validators=[MinValueValidator(0),],
        default=0,
        verbose_name=u'Значение дохода до расширения'
    )
    ODT = models.FloatField(
        validators=[MinValueValidator(0),],
        default=0,
        verbose_name=u'Значения дохода после расширения!!!'
    )

    cp = models.FloatField(default=0, verbose_name=u'Прибль в $')


class MainPeriod(models.Model):
    op = models.FloatField(
        validators=[MinValueValidator(0), ],
        default=0,
        verbose_name=u'Значение колечества лет основного периода'
    )


class MP(models.Model):
    op = models.FloatField(
        validators=[MinValueValidator(0), ],
        default=0,
        verbose_name=u'Значение колечества лет основного периода'
    )