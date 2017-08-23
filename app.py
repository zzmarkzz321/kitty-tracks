#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request, render_template, \
                  session, redirect, url_for, jsonify
from flask_pymongo import PyMongo
import logging
from logging import Formatter, FileHandler
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

try:
    MONGO_URL = os.environ.get('MONGO_URL')
    if not MONGO_URL:
        MONGO_URL = "mongodb://localhost:27017/kittyTracks"

    app.config['MONGO_DBNAME'] = 'kittytracks'
    app.config['MONGO_URI'] = MONGO_URL
    mongo = PyMongo(app)
except:
    print('error connecting to mongodb')

#----------------------------------------------------------------------------#
# Temp Endpoints
#----------------------------------------------------------------------------#

@app.route('/')
def index():
    return 'hello'

'''
    Grabs all or selected lines
'''
@app.route('/kittyTracks/api/v1.0/lines')
def getLines():
    lines = request.args.get('filter')
    message = ''
    results = []

    Lines = mongo.db.kittytracks
    for r in Lines.find():
        results.append({
            'line': r['line'],
            'availability': r['availability'],
            'stops': r['stops']
        })

    return jsonify({'message': message, 'results': results}), 200

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()