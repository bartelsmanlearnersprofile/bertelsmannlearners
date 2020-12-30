import json

from flask import jsonify
from flask_restful import Resource, reqparse, request, abort
from flask_httpauth import HTTPBasicAuth
from sqlalchemy.exc import StatementError, InvalidRequestError, OperationalError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sampledata.data import *
from FlaskAPI.model import Learner, db, learner_schema

auth = HTTPBasicAuth()


class LearnerAPI(Resource):
    # method_decorators = [auth.login_required]

    def __init__(self):
        super(LearnerAPI, self).__init__()

    def get(self):
        if request.method == 'GET':
            try:
                slack_id = request.args.get('slackname')
                print(f"Slackname: {slack_id}")
                if slack_id:
                    learner = db.session.query(Learner.slackname).filter(Learner.slackname == slack_id).one_or_none()
                    print(f"Inside the get command")
                    if learner is not None:
                        return SampleData.single_return_success_data
            except NoResultFound:
                return SampleData.not_found
            except MultipleResultsFound:
                return SampleData.not_found
        else:
            return SampleData.bad_request

    def put(self, slackname):
        if request.method == 'PUT':
            try:
                data = request.get_json()
                print(f"data: {data}") # TODO: Remove
                if data and len(data['data']) == 1:
                    print("Inside the update method") # TODO: Remove
                    for k in data['data']:
                        db.session.query(Learner)\
                            .filter(Learner.slackname == slackname)\
                            .update(data['data'][0])
                        db.session.commit()
                    update = db.session.query(Learner).filter(Learner.slackname == slackname).one_or_none()
                    print(f"Update Info: {dict(update.__dict__)}") # TODO: Remove
                    return "Success", 200
                else:
                    abort(400)
            except ValueError:
                db.session.rollback()
                abort(500)
            except InvalidRequestError:
                db.session.rollback()
                abort(400)

        else:
            abort(502)

    def delete(self, slackname):
        if request.method == 'DELETE':
            try:
                remove_learner = db.session.query(Learner).filter(Learner.slackname == slackname).delete()
                if remove_learner == 1:
                    check = db.session.query(Learner).filter(Learner.slackname == slackname).one_or_none()
                    if check is None:
                        db.session.commit()
                        return "Success", 200
                    else:
                        db.session.rollback()
                        abort(500)
                else:
                    db.session.rollback()
                    abort(400)
            except OperationalError:
                abort(404)
