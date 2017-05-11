#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    File name: config.py
    Author: Ronan Lachater
    Date created: 05/12/2017
    Date last modified: --/--/----
    Python Version: 3.x
'''

mongo_uri = 'mongodb://localhost:27017/db_wine_admin'
mongo_db = 'db_wine_admin'

api_base_url = '/wine/admin'
es_base_url = {
    'host': 'localhost',
    'port': '9200',
    'base': 'http://localhost:9200/db_wine_admin',
    'index': 'db_wine_admin'
}
