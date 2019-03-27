# -*- coding: utf-8 -*-

from dataclasses import dataclass, field


@dataclass(frozen = True)
class ReviewParameters:
    game: str = field(default=None, metadata={"description":
          "Title of the game"})

    subtitle: str = field(default=None, metadata={"description":
          "Subtitle of the game if applicable; None otherwise"})

    releasedate: str = field(default=None, metadata={"description":
         "Release date"})

    genres: set[str] = field(default=None, metadata={"description":
          "Genres as a set"})

    url: str = field(default=None, metadata={"description":
         "Review site name"})

    score: float = field(default=None, metadata={"description":
         "Review score of the game out of 100"})

    # Overridden functions

    def __str__(self):
        return "Game: {0} Site: {1} Score: {2}".format(self.game,
                      self.url, self.score)
