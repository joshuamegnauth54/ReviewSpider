# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Dict


@dataclass(eq=False)
class SpiderSettings:
    __slots__ = ("title", "subtitle", "releasedate", "genres", "score",
                 "developer", "publisher", "sales", "startindex", "sitename",
                 "reviewhint", "buffersize", "scrapyopts")

    title: str
    subtitle: str
    releasedate: str
    genres: str
    score: str
    developer: str
    publisher: str
    sales: str

    startindex: str
    reviewhint: str
    sitename: str
    buffersize: int
    scrapyopts: Dict[str, any]
