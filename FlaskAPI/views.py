from flask import Flask, render_template, request, session, logging, jsonify, abort
from FlaskAPI import app
from flask_restful import Api
from flask_cors import CORS

from FlaskAPI.api_classes import LearnerAPI, LearnerListAPI

CORS(app)
api = Api(app)

api.add_resource(
    LearnerAPI,
    '/api/v1.0/learners/students?slackname=<string:slackname>',
    '/api/v1.0/learners/students?firstname=<string:firstname>&lastname=<string:lastname>&slackname=<string:slackname>',
    '/api/v1.0/learners/students?firstname=<string:firstname>',
    '/api/v1.0/learners/students?lastname=<string:lastname>',
    endpoint='students')
api.add_resource(LearnerListAPI, '/api/v1.0/learners/students', endpoint='student')


# default landing page for the api app
@app.route('/')
@app.route('/home')
def Index():
    """
    defautl page for app
    :return: home template
    """
    return render_template('home.html')
