# -*- coding: utf-8 -*-

from dataclasses import dataclass, field


@dataclass(unsafe_hash=True)
class ReviewParameters:
    __slots__ = ("title", "subtitle", "releasedate", "genres", "sitename",
                 "url", "score", "developer", "publisher", "sales")

    title: str
    subtitle: str
    releasedate: str
    genres: str
    sitename: str
    url: str
    score: float
    developer: str
    publisher: str
    sales: int

    # Overridden functions

    def __str__(self):
        return "Game: {0} Site: {1} Score: {2}".format(self.game,
                                                       self.url, self.score)

# =============================================================================
# The equality operator only needs to ensure that the title, release date,
# site, and review score are equal. We don't need to check the genre as
# the objects are equal if it's the same score from the same site for
# the same game.
# =============================================================================

    def __eq__(self, other):
        return (self.title == other.title
                and self.releasedate == other.releasedate
                and self.sitename == other.sitename
                and self.score == other.score)

    def __ne__(self, other):
        return not self.__eq__(other)

# =============================================================================
# Alphabetical order.
#
# If the titles are equal then the subtitles are the tiebreakers.
# We could also add the strings and perform the comparison. This way
# seems neater.
# =============================================================================

    def __lt__(self, other):
        if (self.title == other.title):
            return self.subtitle < other.subtitle
        return self.title < other.subtitle

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        if (self.title == other.title):
            return self.subtitle <= other.subtitle
        return self.title <= other.subtitle

    def __ge__(self, other):
        return other <= self
