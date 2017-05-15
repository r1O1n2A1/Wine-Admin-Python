#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    File name: elasticsearchUtil.py
    Author: Ronan Lachater
    Date created: 05/12/2017
    Date last modified: --/--/----
    Python Version: 3.x
'''

import logging
import requests
import json
# import multiprocessing as mp

from ... import config
from backend.utils import constantsUtil

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch import helpers

es = Elasticsearch([{
    'host': config.es_base_url['host'],
    'port': config.es_base_url['port']
}])

# pool = mp.Pool(processes=4)

'''
Utils class to call REST API from Elasticsearch
'''
class ElasticsearchUtil:
    def getSearchAll():
        result = []
        logging.debug('ES-Module: Call REST - GET global query')
        res = helpers.scan(es,
            query={"query":{"match_all":{}}},
            index=config.es_base_url['index'],
            scroll=u'480m')
        for hit in res:
            result.append(hit)
        return result

    def getSearchCountAll():
        logging.debug('ES-Module: Call REST to count all users')
        res = es.search(
            config.es_base_url['index'],
            body={"query": {"match_all":{}}},
            size=0
            )
        return res

    def getActiveUsers():
        logging.debug('ES-Module: Call REST to get all active users')
        registeredUsers = es.search(
            config.es_base_url['index'],
            body=constantsUtil.queryActiveUser,
            size=0
        )
        return registeredUsers

    def getLoginLastMonth():
        logging.debug('ES-Module: Call REST to get last month new users')
        lastMonthRegisteredUsers = es.search(
            config.es_base_url['index'],
            body=constantsUtil.queryLoginLastMonth,
            size=0
        )
        return lastMonthRegisteredUsers
