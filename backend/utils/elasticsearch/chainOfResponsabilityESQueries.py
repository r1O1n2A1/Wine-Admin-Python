#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    File name: chainOfResponsabilityESQueries.py
    Author: Ronan Lachater
    Date created: 05/12/2017
    Date last modified: --/--/----
    Python Version: 3.x
'''
import logging
from .. import constantsUtil
from ..exception import customException
from .catalogParsingQueries import CatalogParsingQueries
class Handler(object):
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        res = self._handle(request)
        if not res:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')

class MetaHandler(Handler):
    def _handle(self, request):
        if not constantsUtil.JSON_ES_QUERY:
            return  customException.CustomError('Empty query - could not + \
                    not be processed', constantsUtil.CODE_PARSING)
        else:
            if type(request) == list and  '_source' in request:
                return "processed _source MetaHandler"
            elif type(request) == list and '_id' in request:
                return "processed _id MetaHandler"
        return False

class UserHandler(Handler):
    def _handle(self, request):
        if not constantsUtil.JSON_ES_QUERY:
            return  customException.CustomError('Empty query - could not + \
                not be processed',  constantsUtil.CODE_PARSING)
        else:
            if type(request) == list and 'signUpLastMonth' in request:
                CatalogParsingQueries('dashboard_new_visits_month').main_parsing()
                return "not processed user"
            else:
                return " empty user"
        return False

class OrderHandler(Handler):
    def _handle(self, request):
        if not constantsUtil.JSON_ES_QUERY:
            return  customException.CustomError('Empty query - could not + \
                    not be processed',  constantsUtil.CODE_PARSING)
        else:
            if type(request) == list and 'purchaseLastMonth' in request:
                CatalogParsingQueries('dashboard_purchases_month').main_parsing()
                return "not processed order"
            else:
                return " empty order"
        return False

class Client(object):

    def __init__(self):
        self.handler = MetaHandler(UserHandler(OrderHandler()))

    def delegate(self, request):
        if type(request) == list:
            self.handler.handle(request)
        else:
            logging.debug('chainOfResponsability: not processed')
            return "not processed by chain of responsability impl"
