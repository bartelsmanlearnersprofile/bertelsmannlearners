import json

from flask import jsonify
from flask_restful import Resource, reqparse, request, abort
from flask_httpauth import HTTPBasicAuth
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sampledata.data import *
from FlaskAPI.model import Learner, db, learner_schema

auth = HTTPBasicAuth()


class LearnerListAPI(Resource):
    # method_decorators = [auth.login_required]

    def __init__(self):
        super(LearnerListAPI, self).__init__()

    def get(self):
        if request.method == 'GET':
            try:
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
            except ValueError:
                return json.dumps(SampleData.internal_server_error)
        else:
            return jsonify(SampleData.bad_gateway)

    def post(self):
        if request.method == 'POST':
            data_load = []
            try:
                data = request.get_json()
                print(f"Data: {data}")  # TODO: Remove
                if data:
                    for k in data['data']:
                        if db.session.query(Learner.slackname).filter(Learner.slackname == k['slackname']).first():
                            print("Error raised!") # TODO: Remove
                            abort(400, reason=SampleData.bad_request)
                        else:
                            data_load = [Learner(slackname=k['slackname'],
                                                 firstname=k['firstname'],
                                                 lastname=k['lastname']) for k in data['data']]
                    response = [{'slackname': k['slackname'],
                                 'firstname': k['firstname'],
                                 'lastname': k['lastname']} for k in data['data']]
                    db.session.add_all(data_load)
                    db.session.commit()
                    return jsonify({
                        "status": "success",
                        "status_code": 200,
                        "total": len(response),
                        "data": response
                    })
            except ValueError:
                return SampleData.bad_request
        else:
            return SampleData.bad_gateway
