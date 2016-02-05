#!/usr/bin/python
# -*- coding: utf-8 -*-
from distutils.core import setup

module_name = 'xltasks'
module_version = '0.0.1'

setup(name=module_name,
      version=module_version,
      py_modules=['xltasks'],
      requires=['sqlobject', 'BeautifulSoup4'])