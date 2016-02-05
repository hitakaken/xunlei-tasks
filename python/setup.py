#!/usr/bin/python
# -*- coding: utf-8 -*-
from distutils.core import setup

module_name = 'xunleidata'
module_version = '0.0.1'

setup(name=module_name,
      version=module_version,
      py_modules=['xunleidata'],
      requires=['sqlobject'])