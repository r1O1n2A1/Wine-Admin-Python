#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    File name: constantsUtil.py
    Author: Ronan Lachater
    Date created: 05/12/2017
    Date last modified: --/--/----
    Python Version: 3.x
'''

global JSON_ES_QUERY
global ARRAY_ES_RESULT

es_query_return = {
    'hits': 'hits'
}

queryActiveUser = {
    "query": {
      "filtered": {
         "query": {
            "match_all": {}
         },
         "filter": {
            "missing": {
                "field": "user.desinscription"
            }
         }
      }
    }
}
