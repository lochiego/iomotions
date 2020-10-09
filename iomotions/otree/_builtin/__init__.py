# Don't change anything in this file.
import otree.views
from django.http import HttpRequest
from otree.api import models


class Page(otree.views.Page):
    subsession: models.BaseSubsession
    group: models.BaseGroup
    player: models.BasePlayer
    request: HttpRequest


class WaitPage(Page):
    subsession: models.BaseSubsession
    group: models.BaseGroup


class Bot(otree.api.Bot):
    subsession: models.BaseSubsession
    group: models.BaseGroup
    player: models.BasePlayer
