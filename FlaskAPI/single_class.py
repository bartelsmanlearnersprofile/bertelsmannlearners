from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, request, abort
from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from FlaskAPI.model import Learner, db, learner_schema
from sampledata.data import *

auth = HTTPBasicAuth()


class LearnerAPI(Resource):
    # method_decorators = [auth.login_required]

    def __init__(self):
        super(LearnerAPI, self).__init__()

    def get(self, slackname):
        if request.method == 'GET':
            try:
                # slack_id = request.args.get('slackname')
                print(f"Slackname: {slackname}")
                if slackname:
                    learner = db.session.query(Learner).filter(Learner.slackname == slackname).one_or_none()
                    print(f"Inside the get command: {learner_schema.dump(learner)}")  # TODO: Remove
                    if learner is not None:
                        return jsonify({
                            "status": "success",
                            "status_code": 200,
                            "data": [learner_schema.dump(learner)]
                        })
                    else:
                        # abort(404)
                        return SampleData.not_found
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
                print(f"data: {data}")  # TODO: Remove
                if data and len(data['data']) == 1:
                    print("Inside the update method")  # TODO: Remove
                    for k in data['data']:
                        db.session.query(Learner) \
                            .filter(Learner.slackname == slackname) \
                            .update(data['data'][0])
                        db.session.commit()
                    update = db.session.query(Learner)\
                        .filter(Learner.slackname == slackname).one_or_none()
                    print(f"Update Info: {learner_schema.dump(update)}")  # TODO: Remove
                    return jsonify({
                        "status": "success",
                        "status_code": 200,
                        "data": [learner_schema.dump(update)]
                    })
                else:
                    return SampleData.bad_request
            except ValueError:
                db.session.rollback()
                abort(500, reason=SampleData.internal_server_error)
            except InvalidRequestError:
                db.session.rollback()
                abort(400, reason=SampleData.bad_request)

        else:
            abort(502, reason=SampleData.bad_gateway)

    def delete(self, slackname):
        if request.method == 'DELETE':
            try:
                remove_learner = db.session.query(Learner)\
                    .filter(Learner.slackname == slackname).delete()
                if remove_learner == 1:
                    check = db.session.query(Learner)\
                        .filter(Learner.slackname == slackname).one_or_none()
                    if check is None:
                        db.session.commit()
                        return jsonify({
                            "status": "success",
                            "status_code": 200
                        })
                    else:
                        db.session.rollback()
                        abort(500, reason=SampleData.internal_server_error)
                else:
                    db.session.rollback()
                    abort(400, reason=SampleData.bad_request)
            except OperationalError:
                abort(500, reason=SampleData.internal_server_error)
        else:
            abort(502, reason=SampleData.bad_gateway)
