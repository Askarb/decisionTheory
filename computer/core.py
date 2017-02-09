from computer.models import *


def cp():
    res = ConditionalProfit.objects.all()
    for i in res:
        i.cp = round(i.conditionalProfit, 3)
    return res


def wp():
    res = cp()
    for i in res:
        i.wp = round(i.cp*i.probability, 3)
    return res


def emv():
    emv = []
    for i in ActionList.objects.all():
        s = 0
        for j in wp():
            if i == j.action:
                s += j.wp
        emv.append([i.action, s])
    return emv


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


def check_propability():
    s = 0
    events = EventList.objects.all()
    for i in events:
        s += i.probability
    return s


def cp_max():
    event = EventList.objects.all()
    res = []
    for i in event:
        s = 0
        for j in cp():
            if i == j.event:
                if j.conditionalProfit > s:
                    s = j.cp
        res.append([i.event, s])
    return res


def col():
    res = cp()
    for i in res:
        for j in cp_max():
            if str(j[0]) == str(i.event):
                i.col = round(j[1]-i.cp, 3)
                i.wol = round(i.col * i.probability, 3)
                i.conditionalProfit = round(i.conditionalProfit, 3)
    return res


def eol():
    res = []
    Col = col()
    for j in ActionList.objects.all():
        s = 0
        for i in Col:
            if j == i.action:
                s += i.wol
        res.append([j, round(s, 3)])
    return res


def min_eol():
    min = 999999999999
    for i in eol():
        if min > (i[1]):
            min = i[1]
    return round(min, 3)


def eol_report():
    min = min_eol()
    for i in eol():
        if min == (i[1]):
            return {
                'action': i[0],
                'cp': i[1],
            }
    return {}


