from flask import Flask, render_template, request, session, logging, jsonify, abort
from FlaskAPI import app
from flask_restful import Api, reqparse, request
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth

from FlaskAPI.api_classes import LearnerAPI, LearnerListAPI

CORS(app)
api = Api(app)

api.add_resource(LearnerAPI, '/api/v1.0/learners/students/<string:slackname>', endpoint='students')
api.add_resource(LearnerListAPI, '/api/v1.0/learners/students', endpoint='student')


# default landing page for the api app
@app.route('/')
@app.route('/home')
def Index():
    """
    defautl page for app
    :return: home template
    """
    pass
