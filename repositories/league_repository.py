from db.run_sql import run_sql
from models.team import Team
from models.match import Match
from models.league import League

def save(league):
    sql = "INSERT INTO leagues(name, year) VALUES (%s, %s) RETURNING id"
    values = [league.name, league.year]
    results = run_sql(sql, values)
    league.id = results[0]['id']
    return league

def select_all():
    leagues = []

    sql = "SELECT * FROM leagues"
    results = run_sql(sql)

    for row in results:
        league = League(row['name'], row['year'], row['id'])
        leagues.append(league)
    return leagues

def select(id):
    league = None
    sql = "SELECT * FROM leagues WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        league = League(result['name'], result['year'], result['id'])
    return league

def delete_all():
    sql = "DELETE FROM leagues"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM leagues WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(league):
    sql = "UPDATE leagues SET (name, year) = (%s, %s) WHERE id = %s"
    values = [league.name, league.year, league.id]
    run_sql(sql, values)

# def teams(league):
#     teams = []
#     sql = "SELECT teams.* FROM teams INNER JOIN matches ON matches.team_id = team.id WHERE visits.location_id = %s"
#     values = [league.id]
#     results = run_sql(sql, values)

#     for row in results:
#         team = Team(row['city'], row['name'], row['points'], row['league'], row['id'])
#         teams.append(team)

#     return teams