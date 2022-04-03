# ---- YOUR APP STARTS HERE ----
# -- Import section --
from operator import mod
from flask import Flask
from flask import render_template, url_for
from flask import request, redirect, session
from flask_pymongo import PyMongo
from flask import make_response
from model import Shopping_Cart, can_add
from flask_session import Session
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
#db.create_collection('sessions')
## -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    resp = make_response(render_template('index.html', count = request.cookies.get('count')))
    if 'cart' not in request.cookies:
        resp.set_cookie('cart', json.dumps({}))
        resp.set_cookie('count', '0')
        resp.set_cookie('total', '0')
    return resp

@app.route('/<department>')
def department_view(department):
    instruments = inv.find({'category': department})
    return render_template('department.html', instruments = instruments, count = request.cookies.get('count'))


@app.route('/<department>/<model_number>', methods=['GET', 'POST'])
def instrument_view(department, model_number):
    instrument = inv.find_one({'model_number': str(model_number)})
    if not instrument:
        return 'invalid page id'
    if instrument['category'] != department:
        return f"{model_number} not in this department"
    return render_template('instrument.html', instrument = instrument, count = request.cookies.get('count'))


@app.route('/shopping_cart')
def shopping_cart_view():
    return render_template('shopping_cart.html', count = request.cookies.get('count'))

@app.route('/create_cart')
def create_cart():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('cart', json.dumps({}))
    resp.set_cookie('count', '0')
    resp.set_cookie('total', '0')
    return 'created cookies'

@app.route('/add_to_cart/<department>/<model_number>',  methods=['GET', 'POST'])
def add_to_cart(department, model_number):
    cart = json.loads(request.cookies.get('cart'))
    count = int(request.cookies.get('count'))
    if can_add(cart, model_number):
        if model_number in cart:
            cart[model_number] += 1
        else:
            cart[model_number] = 1
    resp = make_response(redirect(url_for('instrument_view', department=department, model_number=model_number)))
    resp.set_cookie('cart', json.dumps(cart))
    resp.set_cookie('count', str(count + 1))
    return resp
    return redirect(url_for('instrument_view', department=department, model_number=model_number))