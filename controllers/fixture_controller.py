from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.wrappers import Request
from werkzeug.utils import redirect
from models.team import Team
from models.fixture import Fixture
from repositories import team_repositories
from repositories import fixture_repositories

fixture_blueprint = Blueprint("fixtures", __name__)

@fixture_blueprint.route("/teams/<id>/fixtures/")
def fixtures():
    fixtures = fixture_repositories.select_all()
    return render_template("fixtures/index.html", fixtures = fixtures)

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

