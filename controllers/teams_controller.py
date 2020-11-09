from flask import Flask, Blueprint, request, redirect, render_template
from repositories import team_repository, match_repository, league_repository
from models.team import Team

teams_blueprint = Blueprint("teams", __name__)

# INDEX
# GET '/teams'
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", all_teams=teams)

# # NEW
# # GET '/teams/new'
# @teams_blueprint.route("/teams/new", methods=["GET"])    ????
# def new_team():
#     teams = team_repository.select_all

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