from flask import Flask
from flask.ext.bower import Bower

app = Flask(__name__, static_url_path='/static')


from app import views