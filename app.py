from functools import cached_property
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
    items = make_item_list()
    prices = make_price_list() 
    quantities = make_quantity_list()
    print(items)
    print(type(items))
    print(prices)
    print(type(prices))
    print(quantities)
    print(type(quantities))
    return render_template(
        "cart.html",
        items =  items,
        prices = prices, 
        quantities = quantities
        )
    #     item_list = make_list.index(item_list)
    # price_list = make_list.index(price_list)
    # quantity_list = make_list.index(quantity_list)

@app.route("/order")
def order(): #loads order page
   return render_template("order.html")

@app.route("/order_more", methods=["POST"])
def order_more(): #loads order page
   return render_template("order.html", cart = shopping_cart) 

@app.route("/add_item", methods=["POST"])
def add_item():
    global shopping_cart
    food_item = flask.request.form.get("food_item") #what item user orders
    quantity = flask.request.form.get("quantity") # how much of item user orders
    shopping_cart.update({food_item: quantity})
    return render_template("order.html", cart = shopping_cart)

@app.route("/remove_item", methods=["POST"])
def remove_item():
    global shopping_cart
    print(shopping_cart)
    print(type(shopping_cart))
    delete_this = flask.request.form.get("delete_this")
    shopping_cart = shopping_cart.pop(delete_this)  
    item_list = make_item_list()
    price_list = make_price_list()
    quantity_list = make_quantity_list()
    return render_template(
        "cart.html", 
        items = item_list, 
        prices = price_list, 
        quantity_list = quantity_list
        )

@app.route("/clear_cart", methods=["POST"])
def clear_cart(): #loads order page
    global shopping_cart
    shopping_cart={}
    item_list ={}
    price_list = {}
    quantity_list = {}
    return render_template(
        "cart.html",
        items = item_list,
        prices = price_list, 
        quantities = quantity_list
        )

def make_item_list():
    global shopping_cart
    item_list = []
    if shopping_cart:
        filtered_cart = (str(shopping_cart).replace("{","").replace("}", "").replace("'", "")).split(", ")
        for i in filtered_cart:
            item = str((i.split(": "))[0]) 
            item_list.append(item )
    else:
        pass
    return list(item_list)
    
def make_price_list():
    global shopping_cart
    price_list = []
    if shopping_cart:
        filtered_cart = (str(shopping_cart).replace("{","").replace("}", "").replace("'", "")).split(", ")
        for i in filtered_cart:
            item = str((i.split(": "))[0])
            price = menu.get(item)
            price_list.append(price)
    else:
        pass
    return list(price_list)
    
def make_quantity_list():
    global shopping_cart
    quantity_list = []
    if shopping_cart:
        filtered_cart = (str(shopping_cart).replace("{","").replace("}", "").replace("'", "")).split(", ")
        for i in filtered_cart:
            quantity = int((i.split(": "))[1])
            quantity_list.append(quantity)
    else:
        pass
    return list(quantity_list)
    

if __name__ == "__main__":
    app.run()