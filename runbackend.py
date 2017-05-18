#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ronan Lachater, Mehdi Rakrouki"
__copyright__ = "Copyright 2017, The OnWine Project"
__version__ = "1.0.0"
__maintainer__ = "Cyril Deschamp"
__status__ = "dev"


import sys
#-------- define logging properties ------
# define logger
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# set logger in a file
# logging.basicConfig(filename='logs/python.log',level=logging.DEBUG,\
#       format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# création d'un handler qui va rediriger une écriture du log vers
# un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
file_handler = RotatingFileHandler('logs/activity.log', 'a', 1000000, 10)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# set logger in console
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.INFO)
steam_handler.setFormatter(formatter)
logger.addHandler(steam_handler)

from backend import app
if __name__ == '__main__':
    app.run(debug=True)
    
