from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.museum import Museum
from models.work import Work
import repositories.work_repository as work_repository
import repositories.museum_repository as museum_repository

works_blueprint = Blueprint("works", __name__)

# INDEX
# GET '/works
@works_blueprint.route("/works")
def works():
    works = work_repository.select_all()
    return render_template("works/index.html", works = works)

# NEW
# GET '/works/new'
@works_blueprint.route("/works/new", methods = ['GET'])
def new_works():
    museums = museum_repository.select_all()
    return render_template("works/new.html", museums = museums)

# CREATE
# POST '/works'
@works_blueprint.route("/works",  methods=['POST'])
def create_work():
    title = request.form['title']
    artist = request.form['artist']
    year = request.form['year']
    museum = museum_repository.select(request.form['museum_id'])
    work = Work(title, artist, year, museum)
    work_repository.save(work)
    return redirect('/works')

# SHOW
# GET '/works/<id>'
@works_blueprint.route("/works/<id>", methods = ['GET'])
def show(id):
    work = work_repository.select(id)
    return render_template("works/show.html", work = work)


# EDIT
# GET '/works/<id>/edit'
@works_blueprint.route("/works/<id>/edit", methods=['GET'])
def edit_work(id):
    work = work_repository.select(id)
    museums = museum_repository.select_all()
    return render_template('works/edit.html', work = work, museums = museums)


# UPDATE
# PUT '/works/<id>'
@works_blueprint.route("/works/<id>", methods=['POST'])
def update_work(id):
    print(request.form)
    title = request.form["title"]
    artist = request.form["artist"]
    year = request.form["year"]
    museum = museum_repository.select(request.form["museum_id"])
    work = Work(title, artist, year, museum, id)
    work_repository.update(work)
    return redirect('/works')

# DELETE
# DELETE '/works/<id>'
@works_blueprint.route("/works/<id>/delete", methods= ['POST'])
def delete_work(id):
    work_repository.delete(id)
    return redirect("/works")
