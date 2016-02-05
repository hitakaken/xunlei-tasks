#!/usr/bin/python
# -*- coding: utf-8 -*-
from xltasks import XLTaskDb
xunlei = XLTaskDb()
# xunlei.task('d:\\Tools\\', 'http://www.hyqb.sh.cn/', Name='index.html')
xunlei.mirror_ftp('Z:/patent/Data/CN/SIPO', 'patdata1ftp.sipo.gov.cn',
                  encoding='gb2312',
                  dir_filter=lambda name, path:
                  not name.startswith(tuple(['US-TXTO', 'CN-IMGO-10-A', 'CN-IMGO-10-B', 'CN-IMGO-20-U']))
                  and '补充' not in name)
