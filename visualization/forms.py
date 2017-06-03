#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms


class DemoForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()