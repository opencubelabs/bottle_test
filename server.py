from bottle import Bottle, run, route, static_file, request, response, template
from pymongo import MongoClient
from bson.json_util import dumps
import hashlib

app = Bottle(__name__)

client = MongoClient()
db = client.test

@app.route('/')
def root():
	return "Hello from server :)"

@app.route('/hello/<name>')
def hello(name):
	return "Hello "+name+"!"


# Static Routes
@app.route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(jpg|png|gif|ico|svg)>')
def images(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static')

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
