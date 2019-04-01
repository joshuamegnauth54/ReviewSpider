# -*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess

import utils.spiderfactory
from spidersettings import SpiderSettings

# These are just test objects to make it easy to play around in the IPython
# shell

if __name__ == "__main__":
    destructoid = SpiderSettings(title=None,
        subtitle=None,
        releasedate=None,
        genres=None,
        score=None,
        developer=None,
        publisher=None,
        sales=None,
        startindex="https://www.destructoid.com/products-index.phtml" +
        "?filt=reviews&date_s=desc&category=",
        reviewhint=None,
        sitename="Destructoid",
        buffersize=256,
        scrapyopts=utils.spiderfactory.G_SCRAPY_OPTS)

    crawler_proc = CrawlerProcess(destructoid.scrapyopts)