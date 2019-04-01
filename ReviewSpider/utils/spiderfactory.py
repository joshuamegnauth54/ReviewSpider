# -*- coding: utf-8 -*-

from reviewspider import ReviewSpider
from spidersettings import SpiderSettings

G_SCRAPY_OPTS = {"CONCURRENT_ITEMS": 100,
               "CONCURRENT_REQUESTS": 16,
               "CONCURRENT_REQUESTS_PER_DOMAIN": 8,
               "CONCURRENT_REQUESTS_PER_IP": 0,
               "COOKIES_ENABLED": False,
               "REACTOR_THREADPOOL_MAXSIZE": 32,
               "USER_AGENT": "Mozilla/5.0 "
               "(X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"}

def GameSpotSpider():
    pass

def IGNSpider():
    pass

def DestructoidSpider():
    pass

def RockPaperShotgunSpider():
    pass
