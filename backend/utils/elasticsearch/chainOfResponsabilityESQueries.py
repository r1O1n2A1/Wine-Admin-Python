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
import .. from constantsUtil

class Handler(object):

    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        res = self._handle(request)
        if not res:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')

class userHandler(Handler):

    def _handle(self, request):
        if not request:
            return "not empty"
        else:
            return "empty"

''' define other Handlers '''
