from main.models import *


def emv():
    emv = []
    for i in ActionList.objects.all():
        s = 0
        for j in ConditionalProfit.objects.all():
            if i == j.action:
                s += j.probability * j.conditionalProfit
        emv.append([i.action, s])
    return emv


def wp():
    res = ConditionalProfit.objects.all()
    for i in res:
        i.wp = i.conditionalProfit*i.probability
    return res


def emv_max():
    max = -999999999999
    for i in emv():
        if max < (i[1]):
            max = i[1]
    return max


def emv_report():
    max = emv_max()
    for i in emv():
        if max == (i[1]):
            return {
                'action': i[0],
                'cp': i[1],
            }
    return {}


def cp_max():
    event = EventList.objects.all()
    res = []
    for i in event:
        s = 0
        for j in ConditionalProfit.objects.all():
            if i == j.event:
                if j.prize > s:
                    s = j.prize
        res.append([i.event, s])
    return res


def col():
    res = ConditionalProfit.objects.all()
    for i in res:
        for j in cp_max():
            if str(j[0]) == str(i.event):
                i.col = j[1]-i.conditionalProfit
                i.wol = i.col * i.probability
    return res


def eol():
    res = []
    Col = col()
    for j in ActionList.objects.all():
        s = 0
        for i in Col:
            if j == i.action:
                s += i.wol
        res.append([j, s])
    return res


def min_eol():
    min = 999999999999
    for i in eol():
        if min > (i[1]):
            min = i[1]
    return min


def eol_report():
    min = min_eol()
    for i in eol():
        if min == (i[1]):
            return {
                'action': i[0],
                'cp': i[1],
            }
    return {}


def check_propability():
    s = 0
    events = EventList.objects.all()
    for i in events:
        s += i.probability

    return s





