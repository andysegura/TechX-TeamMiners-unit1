# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_pymongo import PyMongo

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "<mongo_uri_here>"

#Initialize PyMongo
mongo = PyMongo(app)

# Comment out this create_collection method after you run the app for the first time
# mongo.db.create_collection('library')

## -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/<department>')
def department_view(department):
    collection = mongo.db.music_store
    instruments = collection.find({'department.html': department})
    return render_template('department.html', instruments = instruments)

@app.route('/<instrument_name>')
def instrument_view(instrument_name):
    collection = mongo.db.music_store
    instrument = collection.find({'name': instrument_name})
    return render_template('instrument.html', instrument = instrument)

@app.route('/shopping_cart')
def shopping_cart_view():
    return render_template('shopping_cart.html')