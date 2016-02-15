#!/usr/bin/python
# -*- coding: utf-8 -*-
from xltasks import XLTaskDb
xunlei = XLTaskDb()
# xunlei.task('d:\\Tools\\', 'http://www.hyqb.sh.cn/', Name='index.html')
# xunlei.mirror_ftp('Z:/patent/Data/CN/SIPO', 'patdata1ftp.sipo.gov.cn',
#                  UserName=***, Password=***, encoding='gb2312',
#                  dir_filter=lambda name, path:
#                  not name.startswith(tuple(['US-TXTO', 'CN-IMGO-10-A', 'CN-IMGO-10-B', 'CN-IMGO-20-U']))
#                  and '补充' not in name)

# xunlei.mirror_web_page_links('Z:/patent/Data/US/ReedTech', [
    ## Patents
    ## 'http://patents.reedtech.com/pgyb.php',         # Grant Yellow Book (Single-Page TIFF Images)
    ## 'http://patents.reedtech.com/pgmpi.php',        # Grant (Multi-Page TIFF Images)
    #'http://patents.reedtech.com/pgrbfti.php',      # Grant Red Book (Full Text with Embedded Images)
    #'http://patents.reedtech.com/pgrbft.php',       # Grant Red Book (Full Text)
    #'http://patents.reedtech.com/pgrbbib.php',      # Grant Red Book (Bibliographic Text)
    #'http://patents.reedtech.com/pgocr.php',        # Grant OCR Text
    #'http://patents.reedtech.com/pgog.php',         # Official Gazettes
    ## 'http://patents.reedtech.com/payb.php',         # Application Yellow Book (Single-Page TIFF Images)
    ## 'http://patents.reedtech.com/pampi.php',        # Application Multi-Page TIFF Images
    #'http://patents.reedtech.com/parbfti.php',      # Application Red Book (Full Text with Embedded Images)
    #'http://patents.reedtech.com/parbft.php',       # Application Red Book (Full Text)
    #'http://patents.reedtech.com/parbbib.php',      # Application Red Book (Bibliographic Text)
    #'http://patents.reedtech.com/assignment.php',   # Assignment XML
    #'http://patents.reedtech.com/maintfee.php',     # Maintenance Fee Events
    #'http://patents.reedtech.com/classdata.php',    # Patent Classification Data
    #'http://patents.reedtech.com/ifwpet.php',       # Patent IFW Petition Decisions
    #'http://patents.reedtech.com/pgptab.php',       # PTAB and PRPS Records
    ## Trademarks
    ## 'http://patents.reedtech.com/tmregmpi.php',     # Registration (Multi-Page TIFF Images)
    ## 'http://patents.reedtech.com/tmappi.php',       # Application Images 24 Hour Box (XML/TIFF/JPG)
    #'http://patents.reedtech.com/tmappxml.php',     # Daily XML Files - Applications
    #'http://patents.reedtech.com/tmassign.php',     # Daily XML Files - Assignments (i.e. ownership)
    #'http://patents.reedtech.com/tmttab.php',       # Daily XML Files - Trademark Trial and Appeal Board (TTAB)
#], 'http://patents.reedtech.com/downloads/', sleep=10)

xunlei.mirror_web_site('S:\\Software\\lang\\javascript\\node\\v5.6.0', 'http://npm.taobao.org/mirrors/node/v5.6.0/')

