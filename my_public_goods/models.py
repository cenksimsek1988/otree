from random import randint

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
    Bot)
from otree.app_template import pages

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_public_goods'
    players_per_group = 3
    num_rounds = 50
    endowment = c(100)
    multiplier = 3

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    print('defined fields on the Group')
    pass


class Player(BasePlayer):
    contribution = models.CurrencyField(min=0, max=Constants.endowment)


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.MyPage, {'contribution': randint(0, 100)})
        yield (pages.Results)

