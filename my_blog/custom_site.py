#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 16:46
# @Author  : Demon
# @File    : custom_site.py
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Blog'
    site_title = 'Blog后台管理'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
