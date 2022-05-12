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

# user added items go here
shopping_cart = {} 

menu = { #items and prices
    "Soup": 1,
    "Drink": 3,
    "Meal": 5,
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cart", methods=["POST"])
def cart():
    global shopping_cart
#    current_cart = flask.request.form.get("cart")
    #filtered_cart = str(shopping_cart).replace("{","").replace("}", "").replace("'", "")
    filtered_cart = (str(shopping_cart).replace("{","").replace("}", "").replace("'", "")).split(", ")
    list = []
    for i in filtered_cart:
        list.append( (i.split(": "))[0] + " (x" + (i.split(": "))[1] + ")")

    return render_template("cart.html", cart = list)

@app.route("/order")
def order(): #loads order page
   return render_template("order.html")

@app.route("/order_more", methods=["POST"])
def order_more(): #loads order page
   return render_template("order.html", cart = cart) 

@app.route("/add_item", methods=["POST"])
def add_item():
    global shopping_cart
    food_item = flask.request.form.get("food_item") #what item user orders
    quantity = flask.request.form.get("quantity") # how much of item user orders
    shopping_cart.update({food_item: quantity})
    return render_template("order.html", cart = shopping_cart)

@app.route("/clear_cart", methods=["POST"])
def clear_cart(): #loads order page
    return render_template("cart.html", cart = {})

if __name__ == "__main__":
    app.run()