import flask 
from flask import Flask, redirect, url_for, render_template
import os
# import random
# from urllib import request
# from tmdb  import getData
# from flask_sqlalchemy import SQLAlchemy 

# app = flask.Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_NEW_URL')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = os.getenv('SECRET_KEY')
# db = SQLAlchemy(app)

# class Cart(db.Model):
#     id = db.Column(db.Integer, unique = True, primary_key=True)
#     item = db.Column(db.String(999), nullable=False)
#     quantity = db.Column(db.Integer(420), nullable=False)
# db.create_all()


app = Flask(__name__)

cart = {}

menu = {
    "Soup": 1,
    "Meal": 5,
    "Drink": 3,
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/order", methods=["POST"])
def order(): #loads order page
   return render_template("order.html") 

@app.route("/add_item", methods=["POST"])
def add_item():
    global cart
    food_item = flask.request.form.get("food_item") #what item user orders
    quantity = flask.request.form.get("quantity") # how much of item user orders
    cart.update({food_item : quantity})
    return render_template("order.html", cart = cart)

if __name__ == "__main__":
    app.run()