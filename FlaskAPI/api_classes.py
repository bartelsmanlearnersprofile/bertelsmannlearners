from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


class LearnerAPI(Resource):
    method_decorators = [auth.login_required]

    def get(self, slackname):
        pass

    def put(self, slackname):
        pass

    def delete(self, slackname):
        pass


class LearnerListAPI(Resource):
    method_decorators = [auth.login_required]

    def get(self):
        pass

    def post(self):
        pass