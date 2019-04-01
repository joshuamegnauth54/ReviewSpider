# -*- coding: utf-8 -*-

import numpy as np
from scrapy import Spider
from scrapy import signals
from urllib.parse import urlparse
from scrapy.exceptions import CloseSpider

from reviewparameters import ReviewParameters
from spidersettings import SpiderSettings


class ReviewSpider(Spider):

    __slots__ = ("instancename", "_isrunning", "_buffer", "_bufferpos",
                 "_spideroptions", "_writer", "crawler")

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

        # self._new_buffer()
        self._isrunning = False
        self.setsettings(spider_settings)

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
        self._bufferpos = 0

    def _write_buffer(self):
        self._writer.write(self._buffer, self._bufferpos,
                           self._spideroptions.buffersize)

# =============================================================================
# There's no way to check if a spider is running as far as I know,
# so we do it manually in case we ever need that information.
# =============================================================================
    def _spider_opened(self, spider):
        self.isrunning = True
        self._new_buffer()

    def _spider_closed(self, spider, reason):
        self.isrunning = False
        self.logger.info("Spider '{0}' was closed. Reason: {1}"
                         .format(self.name, reason))
        self._write_buffer()

# =============================================================================
# PUBLIC METHODS
# =============================================================================

    def isrunning(self):
        return self._isrunning

    def setsettings(self, settings):
        if settings is None:
            raise ValueError("Invalid SpiderSettings (None) passed to "
                             "setsettings in {0}.".format(self.name))
        elif not self.isrunning():
            self.allowed_domains = [urlparse(settings.startindex).netloc]

            if settings.scrapyopts is not None:
                self.settings.update(settings.scrapyopts)

            self.custom_settings = settings.scrapyopts
            self._spideroptions = settings
        else:  # To Do: Make new exception class.
            raise RuntimeError("Not allowed: Changing settings while Spider"
                               " is running. Name: " + self.name)

    def stop(self, reason):
        """
        Stops the current spider and submits the gathered data to the writer
        object.

        :param reason: Reason for closing the spider. This is passed to a
        CloseSpider exception.
        """

        raise CloseSpider(reason)


    def dispatch(self, response):
        pass

