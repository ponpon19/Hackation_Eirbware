import random


choose_array = [
    ["Eat a pizza", "Get some sleep"]
    ["Watch Harry Potter", "Watch Twilight"],
    ["Do the Hunger Game", "Be throw in the Maze Runner"],
    ["Express yourself only vith vowel", "Express yourself only with consonant"],
    ["Have a bad plates everytime you go to restaurant", "Arrive at the wrong place when you go oon trip"]
]

def pick_wyr_array():
    return choose_array[random.randint(0, len(choose_array))]

class Player(object):

    def __init__(self, id, socket, name, clues):
        self.socket = socket
        self.id = id
        self.name = name
        self.clues = clues
        self.story_clues = []
        self.team_clues = []
        self.team_found = False

    def set_team(self, team):
        self.team = team

    def get_team(self):
        return self.team

    def check_team(self, team):
        if self.team == team:
            self.team_found = True
            return True
        else:
            return False

    def team_ready(self, players):
        return self.team_found and players[self.team.id]

    def add_story(self, clue):
        self.story_clues.append(clue)

    def get_story(self):
        return self.story_clues

    def add_team(self, clue):
        self.team_clues.append(clue)

    def get_teams(self):
        return self.team_clues

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id


class State():
    WAIT_PLAYERS = 0
    WAIT_NEW_ROUND = 1
    WYR_WAIT = 2


class Game(object):
    def __init__(self):
        self.nb_turn = 0
        self.nb_player = 0
        self.players = {}

    def add_player(self, player, sessionid):
        self.players[sessionid] = player