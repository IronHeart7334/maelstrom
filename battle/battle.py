from utilities import *
from item import Item
from weather import Weather
from teams import EnemyTeam
from output import Op
from character import EnemyCharacter, ENEMY_CACHE
from serialize import AbstractJsonSerialable
import random

"""
The Battle class pits 2 teams
against eachother,
initializing them
and the weather.
"""
class Battle(AbstractJsonSerialable):
    """
    Required kwargs:
    - name : str
    - desc : str
    - prescript : list of str, defaults to []
    - postscript : list of str, defaults to []

    Not sure how I want to pass enemies.
    Sending an enemyteam makes sense,
    but is less memory efficient than creating one upon starting the battle.
    """
    def __init__(self, **kwargs):#name: str, desc: str, script: list, finalAct: list, level: int, enemyNames: list, rewards = []):
        super(Battle, self).__init__(**dict(kwargs, type="Battle"))
        self.name = kwargs["name"]
        self.desc = kwargs["desc"]
        self.prescript = kwargs.get("prescript", [])
        self.postscript = kwargs.get("postscript", [])
        #self.level = level #the level of enemies

        self.forecast = [] # need to make Weather serialize

        self.enemy_team = EnemyTeam(enemyNames, level)

        self.rewards = to_list(rewards)


    @staticmethod
    def loadJson(jdict: dict) -> "Battle":
        jdict["rewards"] = [Item.read_json(data) for data in jdict["rewards"]]
        return Battle(dict)

    def restrict_weather(self, forecast):
        """
        Since most battles can have any
        weather, it only makes sense to
        exclude it from the constructor,
        so here it is
        """
        self.forecast = to_list(forecast)

    def getDisplayData(self):
        """
        gets data for outputting
        """
        ret = [self.name, "\t" + self.desc]
        for member in self.enemy_team.members:
            ret.append("\t* " + member.getShortDesc())
        return ret

    def __str__(self):
        return self.name

    def load_team(self, team):
        """
        Load the player's team
        """
        self.player_team = team

    # stuff down here
    # add random loot
    def check_winner(self):
        """
        Runs when one
        teams loses all
        members.
        """
        if self.player_team.is_up():
            Op.add(self.player_team.name + " won!")
            Op.display()

            for line in self.postscript:
                Op.add(line)
                Op.display()

            for reward in self.rewards:
                if reward != None:
                    reward.give(self.player_team)

    def begin(self):
        """
        Prepare both teams
        for the match.
        """
        for line in self.prescript:
            Op.add(line)
            Op.display()

        self.enemy_team.initialize()
        self.enemy_team.enemy = self.player_team

        self.player_team.initialize()
        self.player_team.enemy = self.enemy_team

        self.enemy_team.displayData()
        self.player_team.displayData()

        self.weather = Weather.generate_random()

        if len(self.forecast) > 0:
            num = 0
            if len(self.forecast) > 1:
                num = random.randrange(0, len(self.forecast) - 1)
            self.weather = self.forecast[num]
        Op.add(self.weather.get_msg())
        Op.display()

    def end(self):
        """
        The stuff that takes place after battle
        """
        xp = self.enemy_team.getXpGiven()
        for member in self.player_team.members:
            member.gainXp(xp)

    def play(self):
        """
        Used to start
        the battle
        """
        self.begin()

        while self.enemy_team.is_up() and self.player_team.is_up():
            self.weather.do_effect(self.enemy_team.members_rem)
            # did the weather defeat them?
            if self.enemy_team.is_up():
                self.enemy_team.doTurn()
                # only bother doing player turn if enemy survives
                # so this way we don't get 'ghost rounds'
                self.weather.do_effect(self.player_team.members_rem)
                if self.player_team.is_up():
                    self.player_team.doTurn()
        self.check_winner()
        self.end()

    @staticmethod
    def generate_random():
        """
        Creates a random level
        """
        enemy_names = []
        num_enemies = random.randint(1, 4)

        EnemyCharacter.load_enemy(all=True)

        for i in range(0, num_enemies):
            enemy_names.append(random.choice(list(ENEMY_CACHE.keys())))

        return Battle("Random encounter", enemy_names, 1)
