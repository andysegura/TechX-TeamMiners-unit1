# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template, url_for
from flask import request, redirect
from flask_pymongo import PyMongo
from flask import make_response
from model import can_add
import certifi
import pymongo
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
orders = db.orders
# Comment out this create_collection method after you run the app for the first time
# mongo.db.create_collection('library')
#db.create_collection('sessions')



## -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    """
    Home page.  Creates shopping cart in cookies if it does not exist currently.

        Parameters
        ----------
        None

        Returns
        -------
        respons that renders index.html template
    """
    resp = make_response(render_template('index.html', count = request.cookies.get('count')))
    if 'cart' not in request.cookies:
        resp.set_cookie('cart', json.dumps({}))
        resp.set_cookie('count', '0')
        resp.set_cookie('total', '0')
    return resp

@app.route('/<department>')
def department_view(department):
    """
    Shows a specific instrument page.  With description, price, and an add to cart button.

        Parameters
        ----------
        department: str

        Returns
        -------
        redirects to shopping cart on success
    """
    instruments = inv.find({'category': department})
    return render_template('department.html',department = department, instruments = instruments, count = request.cookies.get('count'))

@app.route('/<department>/<model_number>', methods=['GET', 'POST'])
def instrument_view(department, model_number):
    """
    Shows a specific instrument page.  With description, price, and an add to cart button.

        Parameters
        ----------
        department: str
        model_number: str

        Returns
        -------
       renders the instrument template taking in the specific instrument
    """
    if 'cart' not in request.cookies:
        return redirect(url_for('index'))
    instrument = inv.find_one({'model_number': str(model_number)})
    if not instrument:
        return 'invalid page id'
    if instrument['category'] != department:
        return f"{model_number} not in this department"
    return render_template('instrument.html', instrument = instrument, count = request.cookies.get('count'))


@app.route('/shopping_cart')
def shopping_cart_view():
    """
    Shows everything in shopping cart, gets the shopping cart from cookie and converts it to a list of cursors that can be used in 
    the html template.

        Parameters
        ----------
        None

        Returns
        -------
        renders template of shopping cart and passes in whats in the shopping cart
    """
    if 'cart' not in request.cookies:
        return redirect(url_for('index'))
    cart = json.loads(request.cookies.get('cart'))
    total = float(request.cookies.get('total'))
    instruments = [(inv.find_one({'model_number': str(model_number)}), quantity) for model_number, quantity in cart.items()]
    return render_template('shopping_cart.html', count = request.cookies.get('count'), instruments = instruments, total = total)


@app.route('/add_to_cart/<department>/<model_number>',  methods=['GET', 'POST'])
def add_to_cart(department, model_number):
    """
    Adds an item to cart or updates the quantity if the item is already in the cart.
        Parameters
        ----------
        department: str
        model_number: str

        Returns
        -------
        respons that redirects to instrument page
    """
    if 'cart' not in request.cookies:
        return redirect(url_for('index'))
    cart = json.loads(request.cookies.get('cart'))
    count = int(request.cookies.get('count'))
    total = float(request.cookies.get('total'))
    instrument = inv.find_one({'model_number': model_number})
    if can_add(cart, model_number):
        if model_number in cart:
            cart[model_number] += 1
            count += 1
            total += instrument['price']
        else:
            cart[model_number] = 1
            count += 1
            total += instrument['price']
    resp = make_response(redirect(url_for('instrument_view', department=department, model_number=model_number)))
    resp.set_cookie('cart', json.dumps(cart))
    resp.set_cookie('count', str(count))
    resp.set_cookie('total', str(total))
    return resp

@app.route('/update_cart', methods=['GET', 'POST'])
def update_cart():
    """
        Used to update the quantities of the items in the shopping cart. 
        If a button is clicked it will update the quantity here either by adding, subtracting or removing.

        Parameters
        ----------
        None
        Returns
        -------
        response that redirects back to the shopping cart
    """
    if 'cart' not in request.cookies:
        return redirect(url_for('index'))
    resp = make_response(redirect(url_for('shopping_cart_view')))
    cart = json.loads(request.cookies.get('cart'))
    count = int(request.cookies.get('count'))
    total = float(request.cookies.get('total'))
    if request.method == 'POST':
        if 'decrease' in request.form:
            model_number = request.form['decrease']
            instrument = inv.find_one({'model_number': model_number})
            if model_number in cart and cart[model_number] > 1:
                cart[model_number] -= 1
                count -= 1
                total -= instrument['price']
            elif model_number in cart:
                del cart[model_number]
                count -= 1
                total -= instrument['price']
        elif 'increase' in request.form:
            model_number = request.form['increase']
            instrument = inv.find_one({'model_number': model_number})
            if can_add(cart, model_number):
                if model_number in cart:
                    cart[model_number] += 1
                    count += 1
                    total += instrument['price']
                else:
                    cart[model_number] = 1
                    count += 1
                    total += instrument['price']
        elif 'remove' in request.form:
            model_number = request.form['remove']
            instrument = inv.find_one({'model_number': model_number})
            if model_number in cart:
                count -= cart[model_number]
                total -= instrument['price'] * cart[model_number]
                del cart[model_number]
        resp.set_cookie('cart', json.dumps(cart))
        resp.set_cookie('count', str(count))
        resp.set_cookie('total', str(total))
    return resp

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """
    Route to display forms for user to enter in shipping address

        Parameters
        ----------
        None
        Returns
        -------
        checkout html template
    """
    if 'cart' not in request.cookies:
        return redirect(url_for('index'))
    if json.loads(request.cookies.get('cart')) == {}:
        return redirect(url_for('shopping_cart_view'))
    return render_template('checkout.html', count = request.cookies.get('count'))

@app.route('/checkout_validate', methods=['GET', 'POST'])
def checkout_validate():
    """
    Checks out by taking all of the request forms and making sure there is still enough stock to checkout the items in the cart.
    Resets the cart to the initial state.  Adds users order to the database

        Parameters
        ----------
        None
        Returns
        -------
        redirects to shopping cart on success else it redirects to checkout again
    """
    if 'cart' not in request.cookies:
        return redirect(url_for('index'))
    resp = make_response(redirect(url_for('shopping_cart_view')))
    cart = json.loads(request.cookies.get('cart'))
    count = int(request.cookies.get('count'))
    total = float(request.cookies.get('total'))
    if request.method == 'POST':
        
        user = {}
        user['first'] = request.form['first']
        user['last'] = request.form['last']
        user['address'] = request.form['address']
        user['city'] = request.form['city']
        user['state'] = request.form['state']
        user['order'] = cart
        user['amount_paid'] = total
        user['quantity'] = count
        if "" in user.values():
            return redirect(url_for('checkout'))
        orders.insert_one(user)
        for model_number, quantity in cart.items():
            instrument = inv.find_one({'model_number': model_number})
            inv.update_one({'model_number': model_number}, {'$set': {'stock': instrument['stock'] - quantity}})
        resp.set_cookie('cart', json.dumps({}))
        resp.set_cookie('count', '0')
        resp.set_cookie('total', '0')
    return resp