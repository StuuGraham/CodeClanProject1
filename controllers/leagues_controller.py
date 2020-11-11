from flask import Flask, Blueprint, request, redirect, render_template
from repositories import league_repository, match_repository, team_repository
from models.league import League

leagues_blueprint = Blueprint("leagues", __name__)

# INDEX
# GET '/leagues'
@leagues_blueprint.route("/leagues")
def leagues():
    leagues = league_repository.select_all()
    return render_template("leagues/index.html", leagues=leagues)

# NEW
# GET '/leagues/new'
@leagues_blueprint.route("/leagues/new", methods=["GET"])
def new_league():
    teams = team_repository.select_all()
    return render_template("leagues/new.html", teams=teams)

# CREATE
# POST '/leagues'
@leagues_blueprint.route("/leagues", methods=["POST"])
def create_league():
    name = request.form["name"]
    year = request.form["year"]

    league = League(name, year)
    league_repository.save(league)
    return redirect ('/leagues')

# SHOW
# GET 'leagues/<id>'
@leagues_blueprint.route("/leagues/<id>", methods=["GET"])
def show_league(id):
    league = league_repository.select(id)
    teams = team_repository.select_all()
    return render_template("leagues/show.html", league=league, teams=teams)

# # DELETE
# # POST '/leagues/<id>'
# @leagues_blueprint.route("/tasks/<id>/delete", methods=["POST"])
# def delete_league(id):
#     league_repository.delete(id)
#     return redirect('/leagues')            Not sure to have a delete league function? Wouldn't want to delete all data from a league calendar??