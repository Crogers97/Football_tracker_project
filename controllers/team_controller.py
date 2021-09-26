from flask import Flask, render_template
from flask import Blueprint
from models.team import Team
from models.fixture import Fixture
from repositories import team_repositories
from repositories import fixture_repositories


teams_blueprint = Blueprint("teams", __name__)
#Home Page
@teams_blueprint.route("/")
def home():
    return render_template("index.html")

#Team page
@teams_blueprint.route("/teams")
def teams():
    teams = team_repositories.select_all()
    return render_template("teams/index.html", all_teams = teams)


