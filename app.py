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

client = MongoClient('mongodb://localhost:27017/')

#----------------------------------------------------------------------------#
# Utility Functions
#----------------------------------------------------------------------------#

'''
    handles the filter parameter in the request 
'''
def filterRequest(filters):
    return

#----------------------------------------------------------------------------#
# Temp Endpoints
#----------------------------------------------------------------------------#

@app.route('/')
def index():
    return 'Hi'

'''
    Grabs all or selected lines

    example url request: /kittyTracks/api/v1.0/lines?
'''
@app.route('/kittyTracks/api/v1.0/lines')
def getLines():
    lines = request.args.get('filter')

    message = ''
    filters = []
    results = []

    Lines = client.kittyTracks.Lines
    for r in Lines.find():
        results.append({
            'line': r['line'],
            'availability': r['availability'],
            'stops': r['stops']
        })

    return jsonify({'message': message, 'results': results}), 200

'''
    Grabs all or stops

    example url request: /kittyTracks/api/v1.0/stops?
'''
@app.route('/kittyTracks/api/v1.0/stops')
def getStops():
    lines = request.args.get('filter')

    message = ''
    filters = []
    results = []

    #Implement logic here

    return jsonify({'message': message, 'results': results}), 200


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()