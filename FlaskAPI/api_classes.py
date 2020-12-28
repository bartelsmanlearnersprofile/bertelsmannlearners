from flask_restful import Resource, reqparse, request
from flask_httpauth import HTTPBasicAuth
from sampledata.data import *
from FlaskAPI.model import Learner, db, learner_schema

auth = HTTPBasicAuth()


class LearnerAPI(Resource):
    method_decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('slackname', type=str, default='', required=False)
        self.reqparse.add_argument('firstname', type=str, default='')
        self.reqparse.add_argument('lastname', type=str, default='')
        super(LearnerAPI, self).__init__()

    def get(self, slackname):
        pass

    def put(self, slackname):
        pass

    def delete(self, slackname):
        pass


class LearnerListAPI(Resource):
    # method_decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('slackname', type=str, required=True, help='No learner slackname is provided.',
                                   location='json')
        self.reqparse.add_argument('firstname', type=str, required=True, help='No first name provided.',
                                   location='json')
        self.reqparse.add_argument('lastname', type=str, required=True, help='No last name provided.', location='json')
        super(LearnerListAPI, self).__init__()

    def get(self):
        learners = db.session.query(Learner).all()
        if len(learners) != 0:
            learner_list = [learner_schema.dump(learner) for learner in learners]
            return {
                'status': 'success',
                'status_code': 200,
                'data': learner_list
            }
        else:
            return {
                'status': 'success',
                'status_code': 404,
                'data': []
            }

    def post(self):
        pass
