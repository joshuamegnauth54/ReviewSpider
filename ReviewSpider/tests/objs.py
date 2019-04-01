# -*- coding: utf-8 -*-

import reviewspider
import reviewparameters
import spidersettings
import utils.spiderfactory

# These are just test objects to make it easy to play around in the IPython
# shell

if __name__ == "__main__":
    destructoid = SpiderSettings(title=None,
        subtitle=None,
        releasedate=None,
        genres=None,
        score=None,
        developer=None,
        sales=None,
        startindex="https://www.destructoid.com/products-index.phtml" +
        "?filt=reviews&date_s=desc&category=",
        reviewhint=None,
        sitename="Destructoid",
        buffersize=256,
        scrapyopts=None)

    spidertest = ReviewSpider("destructoidtest", destructoid)