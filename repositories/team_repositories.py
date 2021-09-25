from db.run_sql import run_sql
from models.team import Team

def save(team):
    sql = "INSERT INTO teams (name, points) VALUES (%s, %s) RETURNING *"
    values =[team.name, team.points]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['points'], row['id'])
        teams.append(team)
    return teams
