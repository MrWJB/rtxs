#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'JiBin Wang'

from polls.models import Choise, Question
from django.http import HttpResponse
from django.utils import timezone

def choice(request):
    q1 = Question.objects.all()
    print(q1)
    f1 = Question.objects.filter(id=1)
    print(f1)
    current_year = timezone.now().year
    print(current_year)
    q2 = Question.objects.get(pub_date__year=current_year)
    print(q2)


    return HttpResponse("执行成功@")
