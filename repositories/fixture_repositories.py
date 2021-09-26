
from db.run_sql import run_sql
from models.fixture import Fixture

def save(fixture):
    sql = "INSERT INTO fixtures ( home_team, away_team, score, result) VALUES (%s, %s, %s, %s) RETURNING *"
    values= [fixture.home_team, fixture.away_team, fixture.score, fixture.result]
    results = run_sql(sql, values)
    id = results[0]['id']
    fixture.id = id
    return fixture

def select_all():
    fixtures= []
    sql= "SELECT * FROM fixtures"
    results = run_sql(sql)

    for row in results:
        fixture = Fixture(row['home_team'], row['away_team'], row['score'], row['result'], row['id'])
        fixtures.append(fixture)
    return fixtures

def update(fixture):
    sql = "UPDATE fixtures SET (home_team, away_team, score, result) = (%s, %s, %s, %s) WHERE id = %s"
    values = [fixture.home_team, fixture.away_team, fixture.result, fixture.id]
    run_sql(sql, values)






