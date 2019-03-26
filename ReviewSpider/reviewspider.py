# -*- coding: utf-8 -*-

import scrappy

import reviewspidersettings

class ReviewSpider(scrappy.Spider):

    def __init__(self, instancename, url,  *args, **kwargs):
        super().__init__(args, kwargs)
        self.name = instancename


# notes
# add reviewspidersettings stuff in class
# write a function to check settings