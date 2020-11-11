from flask import Flask, Blueprint, request, redirect, render_template
from models.match import Match
from models.team import Team
from models.league import League
import repositories.match_repository as match_repository
import repositories.league_repository as league_repository
import repositories.team_repository as team_repository

matches_blueprint = Blueprint("matches", __name__)

# INDEX
# GET '/matches'
@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    return render_template("matches/index.html", matches=matches)

# NEW
# GET '/matches/new'
@matches_blueprint.route("/matches/new", methods=["GET"])
def new_match():
    teams = team_repository.select_all()
    leagues = league_repository.select_all()
    return render_template("matches/new.html", teams=teams, leagues=leagues)

# CREATE
# POST '/matches'
@matches_blueprint.route("/matches", methods=["POST"])
def create_match():
    team1 = request.form["team1"]
    team2 = request.form["team2"]
    league = request.form["league"]

    # league = league_repository.select(league_id) # ????
    match = Match(team1, team2, league)
    match.play_match()
    match_repository.save(match)
    return redirect ('/matches')

# SHOW
# GET 'matches/<id>'
@matches_blueprint.route("/matches/<id>", methods=["GET"])
def show_match(id):
    match = match_repository.select(id)
    return render_template("matches/show.html", match=match)

# # EDIT
# # GET '/matches/<id>'
# @matches_blueprint.route("/matches/<id>/edit", methods=["GET"])
# def edit_match(id):
#     match = match_repository.select(id)
#     teams = team_repository.select_all()
#     leagues = league_repository.select_all()
#     return render_template("matches/edit.html", match=match, teams=teams, leagues=leagues)

# # UPDATE
# # POST '/matches/<id>'
# @matches_blueprint.route("/matches/<id>", methods=["POST"])
# def update_match(id):
#     team1 = request.form["team1"]
#     team2 = request.form["team2"]
#     league = request.form["league"]
#     winner = match.play_match(team1, team2)

#     match = Match(team1, team2, league, winner, id)
#     match_repository.update(match)
#     return redirect('/matches')

# DELETE
# POST '/matches/<id>'
@matches_blueprint.route("/matches/<id>/delete", methods=["POST"])
def delete_match(id):
    match_repository.delete(id)
    return redirect('/matches')