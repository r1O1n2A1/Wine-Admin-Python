# runbackend.py
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
from backend import app
if __name__ == '__main__':
    app.run(debug=True)
