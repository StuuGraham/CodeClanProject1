from db.run_sql import run_sql
from models.team import Team
from models.match import Match
from models.league import League

def save(match):
    sql = "INSERT INTO matches(team1, team2, winner, league) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [match.team1, match.team2, match.winner, match.league]
    results = run_sql(sql, values)
    match.id = results[0]['id']
    return match

def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        match = Match(row['team1'], row['team2'], row['winner'], row['league'], row['id'])
        matches.append(match)
    return matches

def select(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        match = Match(result['team1'], result['team2'], result['winner'], result['league'], result['id'])
    return match

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(match):
    sql = "UPDATE matches SET (team1, team2, winner, league) = (%s, %s, %s, %s) WHERE id = %s"
    values = [match.team1, match.team2, match.winner, match.league, match.id]
    run_sql(sql, values)