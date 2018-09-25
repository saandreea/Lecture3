import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
  flights = db.execute("SELECT * FROM flights").fetchall()
  return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():

  if not request.form.get("name") :
    return render_template("message.html", message= "Error! Please insert your name.")
  name = request.form.get("name").capitalize()

  try:
    flight_id = int(request.form.get("flight_id"))
  except ValueError:
    return render_template("message.html", message= "Error! Invalid flight number.")

  if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
    return render_template("message.html", message = "Error! No such flight with that id.")

  db.execute("INSERT INTO passangers (name, flight_id) VALUES (:name, :flight_id)", {"name": name, "flight_id": flight_id})
  db.commit()
  return render_template("message.html", message="You have successfully booked your flight!")

