import random
from models.team import Team

class Match:
    def __init__(self, team1, team2, league, winner=None, id=None):
        self.team1 = team1
        self.team2 = team2
        self.league = league
        self.winner = winner
        self.id = id

    def play_match(self):
        winner = random.randint(0,1)
        if 0 == winner:
            self.winner = self.team1
        else:
            self.winner = self.team2

    # This will function similar to the Rock, Paper, Scissors homework.
    # Function should take in two teams and produce a winner at random.
    # Will need Randint?