#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request, render_template, \
                  session, redirect, url_for, jsonify
from pymongo import MongoClient
import logging
from logging import Formatter, FileHandler
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

client = MongoClient('mongodb://zzmarkzz321:Password123@ds153123.mlab.com:53123/heroku_mlbsbpc6')
db = client.heroku_mlbsbpc6


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

    Lines = db.Lines
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