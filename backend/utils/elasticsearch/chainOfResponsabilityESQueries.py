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

class Handler(object):

    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        res = self._handle(request)
        if not res:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')

class UserHandler(Handler):

    def _handle(self, request):
        if not constantsUtil.JSON_ES_QUERY:
            return  customException.CustomError('Empty query - could not + \
                not be processed', CustomError)
        else:
            if type(request) == str and request == 'usersInfo' :
                return "not processed user"
            else:
                return "not empty user"
        return ""


class OrderHandler(Handler):

    def _handle(self, request):
        if not request:
            return "empty order"
        else:
            return "not empty order"

class Client(object):

    def __init__(self):
        self.handler = UserHandler()

    def delegate(self, request):
        if type(request) == str:
            self.handler.handle(request)
        else:
            logging.debug('chainOfResponsability: not processed')
            return "not processed"
