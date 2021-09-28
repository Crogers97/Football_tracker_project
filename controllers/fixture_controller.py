from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.wrappers import Request
from werkzeug.utils import redirect
from models.team import Team
from models.fixture import Fixture
from repositories import team_repositories
from repositories import fixture_repositories
import pdb

fixture_blueprint = Blueprint("fixtures", __name__)

@fixture_blueprint.route("/teams/fixtures/<id>")
def fixtures(id):
    fixtures = fixture_repositories.select_all()
    # pdb.set_trace()
    fixtures_for_team = []
    for fixture in fixtures:
        if fixture.home_team == int(id) or fixture.away_team == int(id):
            data = {}
            data['fixture'] = fixture
            data['home_team_name'] = team_repositories.select(fixture.home_team).name
            data['away_team_name'] = team_repositories.select(fixture.away_team).name
            fixtures_for_team.append(data)

    return render_template("fixtures/index.html", fixtures = fixtures_for_team)

#New Fixture
#GET '/teams/new_fixture'
#Takes User to an HTML form
@fixture_blueprint.route("/teams/new_fixture", methods = ['GET'])
def new_fixture():
    fixtures = fixture_repositories.select_all()
    return render_template("fixtures/new_fixture.html", all_fixtures = fixtures)

#Create a new Fixture
#POST '/teams/<id>/fixtures'
#Gets the data from the form, inserts into the database and updates the '/teams/<id>/fixtures' page

@fixture_blueprint.route("/teams/new_fixture", methods=['POST'])
def create_fixture():
    home_team= request.form['home_team']
    away_team = request.form['away_team']
    score = request.form['score']
    result = request.form['request']
    fixture = Fixture(home_team, away_team, score, result)
    fixture_repositories.save(fixture)
    return redirect('/teams/<id>/fixtures')

#UPDATE
#PUT 'teams/<id>'
@fixture_blueprint.route("/teams/new_fixture", methods=['POST'])
def update_fixture(id):
    home_team= request.form['home_team']
    away_team = request.form['away_team']
    score = request.form['score']
    result = request.form['request']
    fixture = Fixture(home_team, away_team, score, result)
    fixture_repositories.update(fixture)
    return redirect('/teams/<id>/fixtures')







