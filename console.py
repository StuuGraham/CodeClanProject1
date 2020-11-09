import pdb
from models.match import Match
from models.team import Team
from models.league import League

import repositories.match_repository as match_repository
import repositories.league_repository as league_repository
import repositories.team_repository as team_repository

#match_repository.delete_all()
league_repository.delete_all()
team_repository.delete_all()

league = League("Call of Duty", "2019/20")
league_repository.save(league)

team1 = Team("Atlanta", "FaZe", 280, league)
team_repository.save(team1)

team2 = Team("Dallas", "Empire", 260, league)
team_repository.save(team2)

team3 = Team("Florida", "Mutineers", 230, league)
team_repository.save(team3)

team4 = Team("Chicago", "Huntsmen", 230, league)
team_repository.save(team4)

team5 = Team("New York", "Subliners", 140, league)
team_repository.save(team5)

team6 = Team("London", "Royal Ravens", 120, league)
team_repository.save(team6)

team7 = Team("Toronto", "Ultra", 120, league)
team_repository.save(team7)

team8 = Team("Minnesota", "Rokkr", 120, league)
team_repository.save(team8)

team9 = Team("LA", "Optic Gaming", 100, league)
team_repository.save(team9)

team10 = Team("Paris", "Legion", 100, league)
team_repository.save(team10)

team11 = Team("Seattle", "Surge", 50, league)
team_repository.save(team11)

team12 = Team("LA", "Guerrillas", 50, league)
team_repository.save(team12)





pdb.set_trace()