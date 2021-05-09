#!/usr/bin/python3
"""display status"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """function for status route that returns the status"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def getCount():
    count_dict = {"amenities": 'Amenity',
                  "cities": 'City',
                  "places": 'Place',
                  "reviews": 'Review',
                  "states": 'State',
                  "users": 'User'}
    for k in count_dict.keys():
        count_dict[k] = storage.count(count_dict.get(k))
    return jsonify(count_dict)
