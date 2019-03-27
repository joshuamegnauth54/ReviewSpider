# -*- coding: utf-8 -*-

import scrappy

import reviewparameters


class ReviewSpider(scrappy.Spider):

    def __init__(self, instancename, parameters, *args, **kwargs):
        super().__init__(args, kwargs)

        self.name = instancename
        self.parameters

    def _checkparameters(parameters):

