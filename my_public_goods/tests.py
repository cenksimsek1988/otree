from random import randint

from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.MyPage, {'contribution': randint(0, 100)})
        yield (pages.Results)
