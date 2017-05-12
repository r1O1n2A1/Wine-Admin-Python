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
        if not request:
            return "empty"
        else:
            return "not empty"

''' define other Handlers '''

class Client(object):

    def __init__(self):
        self.handler = UserHandler()

    def delegate(self, request):
        if type(request) == dict:
            self.handler.handle(request)
        else:
            logging.log('chainOfResponsability: not processed')
            return "not processd"
