from flask import Flask

app = Flask(__name__)

@app.route('/Welcome')
def welcome():
    return "Welcome"

@app.route('/Welcome/Back')
def welcome_back():
    return "Welcome Back"

@app.route('/Welcome/Home')
def welcome_home():
    return "Welcome Home"