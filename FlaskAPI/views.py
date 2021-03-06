from flask_cors import CORS
from flask_restful import Api

from FlaskAPI import app
from FlaskAPI.multi_class import LearnerListAPI
from FlaskAPI.single_class import LearnerAPI

CORS(app)
api = Api(app)

api.add_resource(
    LearnerAPI,
    '/api/v1.0/learners/student/slackname/<string:slackname>',
    '/api/v1.0/learners/student/update/<string:slackname>',
    '/api/v1.0/learners/student/delete/<string:slackname>',
    endpoint='learner')

api.add_resource(
    LearnerListAPI,
    '/api/v1.0/learners/students',
    '/api/v1.0/learners/students/all',
    endpoint='students')

# default landing page for the api app
# @app.route('/')
# @app.route('/home')
# def index():
#     """
#     defautl page for app
#     :return: home template
#     """
#     return render_template('home.html')

