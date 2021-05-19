import os
import json

from flask import Flask, request, redirect, jsonify
from sqlalchemy.sql import functions
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
database = SQLAlchemy(metadata=MetaData(schema="public"))

@dataclass
class User(database.Model):
    id: int
    name: str

    id = database.Column(database.BigInteger(), primary_key=True)
    name = database.Column(database.String(255))


app = Flask(__name__)
app.config.from_json("config.json")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
database.init_app(app)

@app.route("/version")
def version():
	return {"version": "0.1"}

#crud routes
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        data = request.get_json()
        name = data['name']
        User = User(name=name)
        database.session.add(User)
        database.session.commit()

    Users = User.query.all()
    return jsonify(Users)


@app.route("/update", methods=["PUT"])
def update():

    data = request.get_json()
    id_ = data['id']
    name = data['name']
    User = User.query.filter_by(id=id_).first()
    User.name = name
    database.session.commit()
    return redirect("/")


@app.route("/delete", methods=["DELETE"])
def delete():
    data = request.get_json()
    id_ = data['id']
    User = User.query.filter_by(id=id_).first()
    database.session.delete(User)
    database.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run()
