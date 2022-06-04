import os
import random
from urllib import request
from flask_sqlalchemy import SQLAlchemy 
import flask 
from flask import Flask, url_for

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_NEW_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    first_name = db.Column(db.String(99), nullable=False)
    last_name = db.Column(db.String(99), nullable=False)
    address = db.Column(db.String(99), nullable=False)
    city = db.Column(db.String(99), nullable=False)
    state = db.Column(db.String(99), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
db.create_all()

class Menu(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    appetizer_id = db.Column(db.Integer, unique = True)
    soup_id = db.Column(db.Integer, unique = True)
    beef_id = db.Column(db.Integer, unique = True)
    poultry_id = db.Column(db.Integer, unique = True)
    pork_id = db.Column(db.Integer, unique = True)
    seafood_id = db.Column(db.Integer, unique = True)
    vegetable_id = db.Column(db.Integer, unique = True)
    mei_fun_id = db.Column(db.Integer, unique = True)
    pan_fried_noodles_id = db.Column(db.Integer, unique = True)
    lo_mein_id = db.Column(db.Integer, unique = True)
    fried_rice_id = db.Column(db.Integer, unique = True)
    chop_suey_id = db.Column(db.Integer, unique = True)
    chow_mein_id = db.Column(db.Integer, unique = True)
    egg_foo_young_id = db.Column(db.Integer, unique = True)
    spa_cousine_id = db.Column(db.Integer, unique = True)
    family_dinner_cousine_id = db.Column(db.Integer, unique = True)
    chef_speical_id = db.Column(db.Integer, unique = True)
    combo_plate_id = db.Column(db.Integer, unique = True)
    child_plate_id = db.Column(db.Integer, unique = True)
    wing_platter_id = db.Column(db.Integer, unique = True)
    lunch_special_id = db.Column(db.Integer, unique = True)
    beverage_id = db.Column(db.Integer, unique = True)
db.create_all()

class Order(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    first_name = db.Column(db.String(99), nullable=False)
    last_name = db.Column(db.String(99), nullable=False)
    address = db.Column(db.String(99), nullable=False)
    city = db.Column(db.String(99), nullable=False)
    state = db.Column(db.String(99), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    appetizer_id = db.Column(db.Integer, unique = True, nullable=True)
    soup_id = db.Column(db.Integer, unique = True, nullable=True)
    beef_id = db.Column(db.Integer, unique = True, nullable=True)
    poultry_id = db.Column(db.Integer, unique = True, nullable=True)
    pork_id = db.Column(db.Integer, unique = True, nullable=True)
    seafood_id = db.Column(db.Integer, unique = True, nullable=True)
    vegetable_id = db.Column(db.Integer, unique = True, nullable=True)
    mei_fun_id = db.Column(db.Integer, unique = True, nullable=True)
    pan_fried_noodles_id = db.Column(db.Integer, unique = True, nullable=True)
    lo_mein_id = db.Column(db.Integer, unique = True, nullable=True)
    fried_rice_id = db.Column(db.Integer, unique = True, nullable=True)
    chop_suey_id = db.Column(db.Integer, unique = True, nullable=True)
    chow_mein_id = db.Column(db.Integer, unique = True, nullable=True)
    egg_foo_young_id = db.Column(db.Integer, unique = True, nullable=True)
    spa_cousine_id = db.Column(db.Integer, unique = True, nullable=True)
    family_dinner_cousine_id = db.Column(db.Integer, unique = True, nullable=True)
    chef_speical_id = db.Column(db.Integer, unique = True, nullable=True)
    combo_plate_id = db.Column(db.Integer, unique = True, nullable=True)
    child_plate_id = db.Column(db.Integer, unique = True, nullable=True)
    wing_platter_id = db.Column(db.Integer, unique = True, nullable=True)
    lunch_special_id = db.Column(db.Integer, unique = True, nullable=True)
    beverage_id = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class appetizer(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class soup(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class beef(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class poultry(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class pork(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class seafood(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class vegetable(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class mei_fun(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class pan_fried_noodles(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class lo_mein(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class fried_rice(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class chop_suey(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class chow_mein(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class egg_foo_young(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class spa_cousine(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class family_dinner_cousine(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class chef_special(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class combo_plate(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class child_plate(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class wing_platter(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class lunch_special(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()

class beverage(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    price = db.Column(db.Integer, unique = True, nullable=True)
db.create_all()
