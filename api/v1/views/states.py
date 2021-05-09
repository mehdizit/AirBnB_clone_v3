#!/usr/bin/python3
"""states handler"""

from flask import Flask, request, jsonify, abort, make_response
from api.v1.views import app_views
from models import storage
from models.state import State

@app_views.route('/states', methods=['GET', 'POST'])
def all_states():
    """Retrieves the list of all State objects"""
    if request.method == 'GET':
        return jsonify([state.to_dict()
                        for state in storage.all('State').values()])
    if request.method == 'POST':
        if not request.json:
            abort(400, 'Not a JSON')
        new_State = State(**request.get_json())
        new_State.save()
        return make_response(jsonify(new_State.to_dict()), 201)

@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def state(state_id):
    """description"""
    state = storage.get('State', state_id)

    if not state:
        abort(404)
    if request.method == 'GET':
        return make_response(jsonify(state.to_dict()), 200)
    if request.method == 'DELETE':
        storage.delete(state)
        storage.save()
        return make_response(jsonify({}), 200)
    if request.method == 'PUT':
        if not request.json:
            abort(400, "Not a JSON")
        for key, value in request.json.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(state, key, value)
        state.save()
        return make_response(jsonify(state.to_dict()), 200)
