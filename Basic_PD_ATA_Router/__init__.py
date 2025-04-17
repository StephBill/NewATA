from otree.api import *


doc = """
Route participant to either Basic or normal ATA PD experiment
"""


class C(BaseConstants):
    NAME_IN_URL = 'Basic_PD_ATA_Router'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    # @staticmethod
    def creating_session(subsession):
        session = subsession.session
        print("create a session")
        session.vars['basic_pd_ata_simple'] = 0
        session.vars['basic_pd_ata'] = 0

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Redirect(Page):
    # @staticmethod
    # def is_displayed(self):
    #     return  True

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        session = player.session
        print(session)
        ata_simple  = session.vars.get('basic_pd_ata_simple', 0)
        ata_regular  = session.vars.get('basic_pd_ata', 0)
        if (ata_simple%2==0 and ata_regular%2==0 and ata_regular == ata_simple) or (ata_simple%2!=0):
            assigned_app = 'Basic_PD_ATA_Simple'
            session.vars['basic_pd_ata_simple'] = ata_simple + 1
        else:
            assigned_app = 'Basic_PD_ATA'
            session.vars['basic_pd_ata'] = ata_regular + 1
        player.participant.vars['which_app'] = assigned_app
        return assigned_app


page_sequence = [Redirect]
