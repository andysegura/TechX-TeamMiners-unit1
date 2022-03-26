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
app.config['MONGO_URI'] = "<replace_with_real_mongodb_url>"

#Initialize PyMongo
mongo = PyMongo(app)

# -- Routes section --
# INDEX Route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')