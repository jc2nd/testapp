from flask import Flask

testapp = Flask(__name__)

@testapp.route('/')
def hello_world():
    return 'Hello, World!'
