#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'JiBin Wang'

from django.http import HttpResponse

from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world!")


def hello2(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
