import re
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.wrappers import Request
from werkzeug.utils import redirect
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

#New Team 
#GET '/teams/new_team'
#Takes User to an HTML form
@teams_blueprint.route("/teams/new_team", methods = ['GET'])
def new_team():
    teams = team_repositories.select_all()
    return render_template("teams/new_team.html", all_teams = teams)

#Create a new Team
#POST '/teams'
#Gets the data from the form, inserts into the database and updates the '/teams' page

@teams_blueprint.route("/teams", methods=['POST'])
def create_task():
    name= request.form['name']
    points = request.form['points']
    team = Team(name, points)
    team_repositories.save(team)
    return redirect('/teams')

#SHOW
#GET '/teams/<id>'
@teams_blueprint.route("/teams/<id>", methods=['GET'])
def show_team(id):
    team = team_repositories.select(id)
    return render_template('teams/show_team.html', team=team)





#UPDATE
#PUT 'teams/<id>'
@teams_blueprint.route("/teams/<id>", methods=['POST'])
def update_team(id):
    name= request.form['name']
    points = request.form['points']
    team= Team(name, points, id)
    team_repositories.update(team)
    return redirect('/teams')


#EDIT
# GET '/teams/<id>/edit'
@teams_blueprint.route("/teams/<id>/edit", methods=['GET'])
def edit_team(id):
    team = team_repositories.select(id)
    return render_template('teams/edit_team.html', team=team)

#DELETE
#DELETE 'tasks/<id>/delete'
@teams_blueprint.route("/teams/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repositories.delete(id)
    return redirect('/teams')




