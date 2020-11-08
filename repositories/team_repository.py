from db.run_sql import run_sql
from models.team import Team
from models.match import Match

def save(team):
    sql = "INSERT INTO teams(city, name, points) VALUES (%s, %s, %s) RETURNING id"
    values = [team.city, team.name, team.points]
    results = run_sql(sql, values)
    team.id = results[0]['id']
    return team

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['city'], row['name'], row['points'], row['id'])
        teams.append(team)
    return teams

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['city'], result['name'], result['points'], result['id'])
    return team