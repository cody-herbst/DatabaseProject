import sys, os, bottle

sys.path = ['/var/www/DatabaseProject/'] + sys.path 

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))


# ... build or import your bottle application here ...
from bottle import route, template, static_file

@route('/')
def home():
    return static_file('index.html', root='/var/www/DatabaseProject/public_html/')

@route('/hello')
def hello():
    return "Hello World!"

@route('/fuckyou')
def fuckyou():
    return "Fuck YOU!"

# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
