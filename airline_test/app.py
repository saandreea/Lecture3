import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
  flights = db.execute("SELECT * FROM flights").fetchall()
  return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
  if not request.form.get("name"):
    return render_template("message.html", headline = "Error!", message = "Please type passenger name.")
  name = request.form.get("name")

  try:
    flight_id = int(request.form.get("flight_id"))
  except ValueError:
    return render_template("message.html", headline = "Error!", message = "Invalid flight number.")
  
  if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
    return render_template("message.html", headline = "Error!", message = "No such flight with that id.")
  db.execute("INSERT INTO passangers (name, flight_id) VALUES (:name, :flight_id)", {"name": name, "flight_id": flight_id})
  db.commit()
  return render_template("message.html", headline = "Success!", message="You have successfully booked your flight!")

@app.route("/flights")
def flights():
  flights = db.execute("SELECT * FROM flights").fetchall()
  return render_template("flights.html", flights=flights)

@app.route("/flights/<int:zbor_id>")
def zbor(zbor_id):
  flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id": zbor_id}).fetchone()
  if flight is None:
    return render_template("message.html", headline="Error!", message="No such flight.")
  
  passengers = db.execute("SELECT * FROM passangers WHERE flight_id = :id", {"id": zbor_id}).fetchall()

  return render_template("flight.html", flight=flight, passengers=passengers)

