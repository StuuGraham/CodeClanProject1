from flask import Flask, Blueprint, request, redirect, render_template
from repositories import team_repository, match_repository, league_repository
from models.team import Team
from models.league import League

teams_blueprint = Blueprint("teams", __name__)

# INDEX
# GET '/teams'
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", all_teams=teams)

# NEW
# GET '/teams/new'
@teams_blueprint.route("/teams/new", methods=["GET"])
def new_team():
    leagues = league_repository.select_all()
    return render_template("teams/new.html", all_leagues=leagues)

# CREATE
# POST '/teams'
@teams_blueprint.route("/teams", methods=["POST"])
def create_team():
    city = request.form["city"]
    name = request.form["name"]
    points = 0
    league_id = request.form["league_id"]

    league = league_repository.select(league_id) # ????
    team = Team(city, name, points, league)
    team_repository.save(team)
    return redirect ('/teams')

# SHOW
# GET '/teams/<id>'
@teams_blueprint.route("/teams/<id>", methods=["GET"])
def show_team(id):
    team = team_repository.select(id)
    return render_template("teams/show.html", team=team)

# EDIT
# GET '/teams/<id>'
@teams_blueprint.route("teams/<id>/edit", methods=["GET"])
def edit_team(id):
    team = team_repository.select(id)
    leagues = league_repository.select_all()
    return render_template("teams/edit.html", team=team, leagues=leagues)

# UPDATE
# POST '/teams/<id>'
@teams_blueprint.route("/teams/<id>", methods=["POST"])
def update_team(id):
    city = request.form["city"]
    name = request.form["name"]
    points = request.form["points"]
    league_id = request.form["league_id"]

    league = league_repository.select(league_id)
    team = Team(city, name, points, league, id)
    team_repository.update(team)
    return redirect('/teams')

# DELETE
# POST '/teams/<id>'
@teams_blueprint.route("/teams/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')