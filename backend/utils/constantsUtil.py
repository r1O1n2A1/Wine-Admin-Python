#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    File name: constantsUtil.py
    Author: Ronan Lachater
    Date created: 05/12/2017
    Date last modified: --/--/----
    Python Version: 3.x
'''
import time

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

### Queries Elasticsearch
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

queryLoginLastMonth = {
  "query": {
    "filtered": {
      "query": {
        "match_all": {}
      },
      "filter": {
        "range": {
            "user.inscription": {
                  "gte": 1491004800000,
                  "lt": 1493596800000,
                  "format": "epoch_millis"
             }
         }
       }
    }
  }
}


# date to parse
LAST_MONTH_DATE = "01/05/2017"
dateLastMonth = time.strptime(LAST_MONTH_DATE, "%d/%m/%Y")
### ERROR CODE ####
CODE_PARSING = 'Elasticsearch parsing can not be done'
