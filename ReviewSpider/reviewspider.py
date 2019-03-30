# -*- coding: utf-8 -*-

import scrappy

import reviewparameters


class ReviewSpider(scrappy.Spider):

    def __init__(self, instancename, parameters, *args, **kwargs):
        super().__init__(args, kwargs)

        self.name = instancename
        self.parameters = self._checkparameters(parameters)
        urlsplit = str.split(self.parameters.url, "/")

        if (urlsplit[0] == "http"):
            allowed_domains = urlsplit[1]
        else:
            allowed_domains = urlsplit[0]


    def _checkparameters(parameters):
        return parameters #Will implement later if I figure it out

    def dispatch(self, response):
        pass

