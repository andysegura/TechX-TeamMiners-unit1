# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_pymongo import PyMongo
import certifi
import pymongo

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

## -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return str(inv.find_one({}))
    #return render_template('index.html')

@app.route('/<department>')
def department_view(department):
    collection = mongo.db.inventory
    instruments = collection.find({'department.html': department})
    return render_template('department.html', instruments = instruments)

@app.route('/<model_number>')
def instrument_view(model_number):
    collection = mongo.db.inventory
    instrument = collection.find({'model_number': model_number})
    return render_template('instrument.html', instrument = instrument)

@app.route('/shopping_cart')
def shopping_cart_view():
    return render_template('shopping_cart.html')