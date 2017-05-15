#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    File name: constantsUtil.py
    Author: Ronan Lachater
    Date created: 05/12/2017
    Date last modified: --/--/----
    Python Version: 3.x
'''

''' CONFIG File only for ES query + processing '''

# result elasticsearch query JSON format
global JSON_ES_QUERY

# return the results for the init dashboard
ARRAY_ES_RESULT = {

}
# use of the current selected user
global CURRENT_USER

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

### ERROR CODE ####
CODE_PARSING = 'Elasticsearch parsing can not be done'
