import random
from models.team import Team

class Match:

    def play_match(self, team_1, team_2):
        team_1 = 0
        team_2 = 1
        winner = random.randint(0,1)
        if team_1 == winner:
            return team_1 + " wins!"
        else:
            return team_2 + " wins!"

    # This will function similar to the Rock, Paper, Scissors homework.
    # Function should take in two teams and produce a winner at random.
    # Will need Randint?