# -*- coding: utf-8 -*-

import numpy as np
from scrapy import Spider
from scrapy import signals
from urllib.parse import urlparse

import reviewparameters
import spidersettings


class ReviewSpider(Spider):

    def __init__(self, instancename, spider_settings, *args, **kwargs):
        """
        ReviewSpider is a subclass of scrapy.Spider which is designed to scrape
        a site that publishes video game reviews for scores and other data.
        The data is sent to an instance of a thread safe ReviewSpiderWriter
        class.

        :param instancename: A UNIQUE name for this object.
        :param spider_settings: An instance of SpiderSettings; see
        documentation for more details.
        """
        self.name = instancename
        super().__init__(instancename, *args, **kwargs)

# =============================================================================
# We must call super() after setting a name as well as pass a name to
# the constructor. The Spider constructor complains and throws an exception
# if a name isn't found. Names must be unique.
# =============================================================================

        self._new_buffer()
        self.setsettings(spider_settings)
        self._isrunning = False

        self._connectsignals()

# =============================================================================
# Scrapy has a signals API which we make use of for ReviewSpider.
# Signals used: spider_opened, spider_closed
# =============================================================================
    def _connectsignals(self):
        self.crawler.signals.connect(self._spider_opened,
                                     signals.spider_opened)

        self.crawler.signals.connect(self._spider_closed,
                                     signals.spider_closed)

    def _new_buffer(self):
        self._buffer = np.empty(self._spideroptions.buffersize,
                                type("ReviewParameters"))

    def _write_buffer(self):
        self._writer(self._buffer)

# =============================================================================
# There's no way to check if a spider is running as far as I know,
# so we do it manually in case we ever need that information.
# =============================================================================
    def _spider_opened(self, spider):
        self.isrunning = True

    def _spider_closed(self, spider, reason):
        self.isrunning = False
        self.logger.info("Spider '{0}' was closed. Reason: {1}"
                         .format(self.name, reason))

# =============================================================================
# PUBLIC METHODS
# =============================================================================

    def isrunning(self):
        return self.isrunning

    def setsettings(self, settings):
        if settings is None:
            raise ValueError("Invalid SpiderSettings (None) passed to "
                             "setsettings in {0}.".format(self.name))
        elif not self.isrunning():
            self.allowed_domains = [urlparse(settings.startindex).netloc]

            if settings.scrapyopts is not None:
                self.settings.update(settings.scrapyopts)

            self._spideroptions = settings
        else:  # To Do: Make new exception class.
            raise RuntimeError("Not allowed: Changing settings while Spider"
                               " is running. Name: " + self.name)

    def dispatch(self, response):
        pass

