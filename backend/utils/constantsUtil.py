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

queryPriceQuantityRange = {
  "query": {
    "query_string": {
      "query": "*",
      "analyze_wildcard": True
    }
  },
  "size": 0,
  "aggs": {
    "2": {
      "range": {
        "field": "user.order.product.product_price",
        "ranges": [
          {
            "from": 0,
            "to": 50
          },
          {
            "from": 50,
            "to": 100
          },
          {
            "from": 100,
            "to": 150
          },
          {
            "from": 150,
            "to": 10000
          }
        ],
        "keyed": True
      },
      "aggs": {
        "3": {
          "range": {
            "field": "user.order.product.quantity",
            "ranges": [
              {
                "from": 1,
                "to": 5
              },
              {
                "from": 5,
                "to": 10
              },
              {
                "from": 10,
                "to": 100
              }
            ],
            "keyed": True
          }
        }
      }
    }
  }
}

queryWineDistribution = {
  "size": 0,
  "query": {
    "query_string": {
      "analyze_wildcard": True,
      "query": "Vins Blancs"
    }
  },
  "aggs": {
    "2": {
      "terms": {
        "field": "user.order.product.product_type",
        "size": 5,
        "order": {
          "_count": "desc"
        }
      }
    }
  }
}

queryCountryDistribution = {
  "size": 0,
  "query": {
    "query_string": {
      "analyze_wildcard": True,
      "query": "Vins Blancs"
    }
  },
  "aggs": {
    "2": {
      "terms": {
        "field": "user.country",
        "size": 54,
        "order": {
          "_count": "desc"
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
