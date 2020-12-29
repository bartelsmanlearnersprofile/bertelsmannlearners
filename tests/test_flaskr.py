import os
import json
import tempfile
from collections import OrderedDict

import pytest
from flask import jsonify

from FlaskAPI import app
import config
from FlaskAPI.model import db
from sampledata.data import *


user_data = {
        "data": [
            {
                "firstname": "George",
                "lastname": "Udosen",
                "slackname": "udoyen"
            },
            {
                "firstname": "Kenneth",
                "lastname": "Udosen",
                "slackname": "nicce"
            },
            {
                "firstname": "Koo",
                "lastname": "Udosen",
                "slackname": "udoyen1"
            },
            {
                "firstname": "David",
                "lastname": "Ekanem",
                "slackname": "mowa"
            },
        ]
    }


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp(suffix=".db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.config.get('DATABASE')}"

    print(f"Database full path: {app.config.get('SQLALCHEMY_DATABASE_URI')}") # TODO: Remove
    print(f'Database: {app.config.get("DATABASE")}') # TODO: Remove
    print(f'Second field: {db_fd}') # TODO: Remove
    app.config['TESTING'] = config.TestingConfig()

    with app.test_client() as client:
        with app.app_context():
            db.init_app(app)
            db.drop_all()
            db.create_all()
        yield client
    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


# @pytest.mark.skip(reason="Need to test post data addition")
def test_empty_db(client):
    """Start with a blank database."""
    rv = client.get('/api/v1.0/learners/students')
    assert SampleData.not_found == json.loads(rv.data)


def test_db_data_addition(client):
    """
    Used to test data addition to
    database
    :type client: flask test client
    """
    with app.app_context():
        rv = client.post('/api/v1.0/learners/students',
                         data=json.dumps(SampleData.user_data),
                         headers={"Content-Type": "application/json", "Accept": "application/json"})
    print(f"RV: {rv.data}") # TODO: Remove
    assert rv.content_type == 'application/json'
    assert SampleData.multiple_return_success_data == json.loads(rv.data)