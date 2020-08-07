#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 16:30
# @Author  : Demon
# @File    : adminforms.py

from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
