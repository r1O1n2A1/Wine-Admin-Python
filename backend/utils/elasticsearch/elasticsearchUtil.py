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
from ... import config
from backend.utils import constantsUtil

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

es = Elasticsearch([{
    'host': config.es_base_url['host'],
    'port': config.es_base_url['port']
}])

'''
Utils class to call REST API from Elasticsearch
'''
class ElasticsearchUtil:
    def getSearchAll():
        logging.debug('ES-Module: Call REST - GET global query')
        # res = es.search(
        #     config.es_base_url['index'],
        #     body={"query": {"match_all":{}}},
        #     size=1000
        #     )
        s = Search(using=es, index=config.es_base_url['index'])
        # s = s.source([])
        # ids = [h.meta.id for h in s.scan()]
        t = 1
        for hit in s.scan():
                print(hit)

        # print(ids)
        return 'res'

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
        registeredUser = es.search(
            config.es_base_url['index'],
            body=constantsUtil.queryActiveUser,
            size=0
        )
        return registeredUser
