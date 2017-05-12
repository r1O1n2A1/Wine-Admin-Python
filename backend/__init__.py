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
from backend.utils.elasticsearch.catalogParsingQueries import CatalogParsingQueries
from backend.utils.encodingUtil import JSONEncoder
from backend.utils.exception import customException
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
        resultQueryDict = ElasticsearchUtil.getSearchAll()
        # parse in json REST call
        resultQueryJson = json.dumps(resultQueryDict,
            default=json_util.default)
        logging.debug('--------beginning--------')
        constantsUtil.JSON_ES_QUERY = resultQueryJson
        # logging.debug(parsed_json['hits']['hits'][0]['_source']['user'][0]['order'][0]['product'])
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
        # CatalogParsingQueries('dashboard_purchases_month').main_parsing()
        try:
            CatalogParsingQueries('dashboard_parseHitsES').main_parsing()
        except customException.CustomError as customError:
            returnStr = 'query ES can not be processed: ' + str(customError)
        if returnStr != '':
            return returnStr
        return str('working progress...')

    @app.route(config.api_base_url + '/dashboard/init',
        methods=['GET'])
    def initDashboard():
        logging.debug('REST call:  get elasticsearch query / call mongo + \
            to init the OnWine dashboard')
        activeUsers = ElasticsearchUtil.getActiveUsers()
        jsonActiveUsers = json.dumps(activeUsers,
            default=json_util.default)
        return jsonActiveUsers
