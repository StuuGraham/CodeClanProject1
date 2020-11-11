from db.run_sql import run_sql
from models.team import Team
from models.match import Match
from models.league import League
from repositories import league_repository, team_repository

def save(match):
    sql = "INSERT INTO matches(team1_id, team2_id, league_id, winner) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [match.team1.id, match.team2.id, match.league.id, match.winner.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    match.id = id
    return match

def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        team1 = team_repository.select(row['team1_id'])
        team2 = team_repository.select(row['team2_id'])
        league = league_repository.select(row['league_id'])
        match = Match(team1, team2, league, row['winner'], row['id'])
        matches.append(match)
    return matches

def select(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        match = Match(result['team1'], result['team2'], result['league'], result['winner'], result['id'])
    return match

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(match):
    sql = "UPDATE matches SET (team1_id, team2_id, league_id, winner) = (%s, %s, %s, %s) WHERE id = %s"
    values = [match.team1.id, match.team2.id, match.league.id, match.winner, match.id]
    run_sql(sql, values)