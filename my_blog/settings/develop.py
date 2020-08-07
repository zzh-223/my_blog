#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 15:54
# @Author  : Demon
# @File    : develop.py
from .base import *
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


