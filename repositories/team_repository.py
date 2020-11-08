from db.run_sql import run_sql
from models.team import Team
from models.match import Match

def save(team):
    sql = "INSERT INTO teams(city, name, points) VALUES (%s, %s, %s) RETURNING id"
    values = [team.city, team.name, team.points]
    results = run_sql(sql, values)
    team.id = results[0]['id']
    return team