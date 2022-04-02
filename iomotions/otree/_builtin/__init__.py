# Don't change anything in this file.
import otree.views
from otree.api import models
from starlette import requests


class Page(otree.views.Page):
    subsession: models.BaseSubsession
    group: models.BaseGroup
    player: models.BasePlayer
    request: requests.Request


class WaitPage(Page):
    subsession: models.BaseSubsession
    group: models.BaseGroup


class Bot(otree.api.Bot):
    subsession: models.BaseSubsession
    group: models.BaseGroup
    player: models.BasePlayer
