from flask import Flask
from flask.ext.bower import Bower
from flask.ext.cache import Cache

app = Flask(__name__, static_url_path='/static')


# define the cache config keys,
app.config['CACHE_TYPE'] = 'simple'

# register the cache instance and binds it on to your app
app.cache = Cache(app)

from app import views