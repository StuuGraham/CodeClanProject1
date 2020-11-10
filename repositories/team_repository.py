from db.run_sql import run_sql
from models.team import Team
from models.match import Match
from models.league import League
from repositories import league_repository, match_repository

def save(team):
    sql = "INSERT INTO teams(city, name, points, league_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [team.city, team.name, team.points, team.league.id]
    results = run_sql(sql, values)
    team.id = results[0]['id']
    return team

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        league = league_repository.select(row['league_id'])
        team = Team(row['city'], row['name'], row['points'], league, row['id'])
        teams.append(team)
    return teams

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        league = league_repository.select(result['league_id'])
        team = Team(result['city'], result['name'], result['points'], league, result['id'])
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(team):
    sql = "UPDATE team SET (city, name, points, league_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [team.city, team.name, team.points, team.league.id, team.id]
    run_sql(sql, values)