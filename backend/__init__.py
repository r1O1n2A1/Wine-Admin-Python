# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from backend.utils.encoding import JSONEncoder


import logging
from logging.handlers import RotatingFileHandler

#-------- define logging properties ------

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# set logger in a file
# logging.basicConfig(filename='logs/python.log',level=logging.DEBUG,\
#       format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# création d'un handler qui va rediriger une écriture du log vers
# un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
file_handler = RotatingFileHandler('logs/activity.log', 'a', 1000000, 10)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# set logger in console
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.DEBUG)
steam_handler.setFormatter(formatter)
logger.addHandler(steam_handler)

# -------- END loggin properties ---------

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'bd_wine_admin'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/bd_wine_admin'

mongo = PyMongo(app)

class AdminCRUD:
    @app.errorhandler(404)
    def not_found(error):
        return  'this page does not exist', 404


    @app.route('/wine/admin/<login>/<password>',
        methods=['GET'])
    def login(login, password):
        # login = request.args.get('login')
        # password = request.args.get('password')
        logging.debug('REST call: admin with login and password')
        admin = mongo.db.admin.find_one_or_404({"login":login, "password": password})
        if admin is not None:
            return JSONEncoder().encode(admin)
