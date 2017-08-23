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

    Lines = client.kittyTracks.Lines
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

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''