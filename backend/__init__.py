#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    File name: __init__.py
    Author: Ronan Lachater
    Date created: 05/12/2017
    Date last modified: --/--/----
    Python Version: 3.x
'''
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
from bson import json_util
import json
import requests



# add from our architecture
from . import config
from backend.utils import constantsUtil
from backend.utils.elasticsearch.elasticsearchUtil import *
from backend.utils.encodingUtil import JSONEncoder
import logging

# -------- END loggin properties ---------

app = Flask(__name__)
CORS(app)
app.config['MONGO_DBNAME'] = config.mongo_db
app.config['MONGO_URI'] = config.mongo_uri

mongo = PyMongo(app)

class AdminCRUD:
    @app.errorhandler(404)
    def not_found(error):
        return  'this page does not exist', 404


    @app.route(config.api_base_url +'/<login>/<password>',
        methods=['GET'])
    def loginAdmin(login, password):
        # login = request.args.get('login')
        # password = request.args.get('password')
        logging.debug('REST call: admin with login and password')
        admin = mongo.db.admin.find_one_or_404({"login":login, "password": password})
        if admin is not None:
            return json.dumps(admin, default=json_util.default)
            #return JSONEncoder().encode(admin)

class AdminSearch:
    @app.errorhandler(404)
    def not_found(error):
        return 'search returns, no match found', 404

    @app.route(config.api_base_url + '/search/all',
        methods=['GET'])
    def searchAllUsers():
        logging.debug('REST call:  get elasticsearch query for all users')
        users = ElasticsearchUtil.getSearchAll()
        jsonUsers = json.dumps(users,
            default=json_util.default)
        parsed_json = json.loads(jsonUsers)
        logging.debug('--------beginning--------')
        logging.debug(parsed_json['hits']['hits'][0]['_source']['user'][0]['order'][0]['product'])
        # for key,val in parsed_json['hits'].items():
        #     if(key == 'hits'):
        #         logging.debug(val[key].items())
        # for key,role in users.items():
        #     if(key == 'hits'):
        #         for val in role[key]:
        #             for a,role in val.items():
        #                 if (a == '_source'):
        #                         logging.debug(a)
        logging.debug('----------end----------')
        return 'em'

    @app.route(config.api_base_url + '/search/active',
        methods=['GET'])
    def searchDashboardActiveUsers():
        logging.debug('REST call:  get elasticsearch query for active users')
        activeUsers = ElasticsearchUtil.getActiveUsers()
        jsonActiveUsers = json.dumps(activeUsers,
            default=json_util.default)
        return jsonActiveUsers
