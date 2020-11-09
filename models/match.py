import random
from models.team import Team

class Match:
    def __init__(self, team1, team2, winner=None, id=None):
        self.team1 = team1
        self.team2 = team2
        self.winner = winner
        self.id = id

    def play_match(self):
        winner = random.randint(0,1)
        if 0 == winner:
            self.winner = self.team1
            return self.team1.city + self.team1.name + " wins!"
        else:
            self.winner = self.team2
            return self.team2.city + self.team2.name + " wins!"

    # This will function similar to the Rock, Paper, Scissors homework.
    # Function should take in two teams and produce a winner at random.
    # Will need Randint?