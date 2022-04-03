# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect, session
from flask_pymongo import PyMongo
from model import Shopping_Cart
import certifi
import pymongo
import secrets
import json
# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'miners_music'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin:3sAW1DQEaqpfDtqz@cluster0.ma4v1.mongodb.net/lab9database?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app)
client = pymongo.MongoClient("mongodb+srv://admin:3sAW1DQEaqpfDtqz@cluster0.ma4v1.mongodb.net/lab9database?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.miners_music
inv = db.inventory
# Comment out this create_collection method after you run the app for the first time
# mongo.db.create_collection('library')
app.secret_key = secrets.token_urlsafe(16)
## -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    session['cart'] = Shopping_Cart().__dict__
    return render_template('index.html', shopping_cart=session['cart'])

@app.route('/<department>')
def department_view(department):
    collection = mongo.db.inventory
    instruments = collection.find({'category': department})
    return render_template('department.html', instruments = instruments, shopping_cart=session['cart'])

@app.route('/<department>/<model_number>')
def instrument_view(department, model_number):
    collection = db.inventory
    instrument = collection.find_one({'model_number': str(model_number)})
    if not instrument:
        return 'invalid page id'
    if instrument['category'] != department:
        return f"{model_number} not in this department"
    return render_template('instrument.html', instrument = instrument, shopping_cart=session['cart'])

@app.route('/shopping_cart')
def shopping_cart_view():
    return render_template('shopping_cart.html', shopping_cart=session['cart'])