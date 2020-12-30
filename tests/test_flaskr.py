import os
import json
import tempfile
import pytest
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from FlaskAPI import app
import config
from FlaskAPI.model import db
from sampledata.data import *

_cwd = os.path.dirname(os.path.abspath(__file__))


def init_db_from_script(script: str, db: SQLAlchemy) -> bool:
    """Function to load data into sqlite
    database
    Parameters:
        script (str): path to sql file
        db (SQLAlchemy): Sqlalchemy object
    Returns:
        bool: True if successful and False otherwise
        :param script:
        :param db:
        :return:
    """
    # Create an empty command string
    sql_command = ''
    # engine = db.create_engine(script)

    with open(script, 'r') as sql_file:
        # Iterate over all lines in the sql file
        for line in sql_file:
            # Ignore commented lines
            if not line.startswith('--') and line.strip('\n'):
                # Append line to the command string
                sql_command += line.strip('\n')

                # If the command string ends with ';', it is a full statement
                if sql_command.endswith(';'):
                    # Try to execute statement and commit it
                    try:
                        # noinspection SqlAlchemyUnsafeQuery
                        db.engine.execute(text(sql_command))
                        db.session.commit()
                    # Assert in case of error
                    except TypeError as t_err:
                        print("TypeError: {}".format(t_err))
                        return False
                    except ValueError as v_err:
                        print("ValueError: {}".format(v_err))
                        return False
                    except Exception as e_err:
                        print("Exception: {}, {}".format(type(e_err), e_err))
                        return False

                    # Finally, clear command string
                    finally:
                        sql_command = ''


@pytest.fixture
def client():
    """
    Pytest fixture
    """
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
            db_file = os.path.join(_cwd, 'learners.sql')
            init_db_from_script(db_file, db)
        yield client
    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_homepage(client):
    """
    Used to test the home page
    :param client: Flask test client
    """
    rv = client.get('/')
    rm = client.get('/home')

    assert 200 == rm.status_code
    assert 200 == rv.status_code


# @pytest.mark.skip(reason="Need to test post data addition")
def test_db_initialization(client):
    """
    Used to initialize database creation
    :param client: Flask test client
    """
    rv = client.get('/api/v1.0/learners/students/all')
    assert SampleData.database_initialization_success_return == json.loads(rv.data)


# @pytest.mark.skip(reason="Need to test post data addition")
def test_db_multiple_data_addition(client):
    """
    Used to test data addition to
    database
    :param client: flask test client
    """
    with app.app_context():
        rv = client.post('/api/v1.0/learners/students',
                         data=json.dumps(SampleData.user_data),
                         headers={"Content-Type": "application/json", "Accept": "application/json"})
    print(f"RV: {rv.data}") # TODO: Remove
    assert rv.content_type == 'application/json'
    assert SampleData.multiple_return_success_data == json.loads(rv.data)


# @pytest.mark.skip(reason="testing")
def test_get_single_learner(client):
    """
    Used to test if single learner
    can be queried
    :param client: Flask test client
    """
    # with app.app_context():
    rv = client.get('/api/v1.0/learners/student/slackname/udoyen')
    print(f"RV: {rv.data}")
    assert 200 == rv.status_code


# @pytest.mark.skip(reason="testing")
def test_get_nonexistent_single_learner(client):
    """
    Used to test if single learner
    can be queried
    :param client: Flask test client
    """
    # with app.app_context():
    rv = client.get('/api/v1.0/learners/student/slackname/man')
    print(f"RV: {rv.data}")
    assert SampleData.not_found == json.loads(rv.data)


def test_update_learner(client):
    """
    Used to test put requests for
    updating the learner's info
    :param client: flask test client
    """
    rv = client.put('/api/v1.0/learners/student/update/udoyen',
                    data=json.dumps(SampleData.user_update_data),
                    headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert 200 == rv.status_code
    assert rv.content_type == 'application/json'


def test_fail_update_for_multiple_learners(client):
    """
    Used to test multiple learners insertion
    into the database
    :param client: Flask test client
    """
    rv = client.put('/api/v1.0/learners/student/update/udoyen',
                    data=json.dumps(SampleData.multiple_user_update_data),
                    headers={"Content-Type": "application/json", "Accept": "application/json"})
    print(f"rv: {rv.data}")
    assert SampleData.bad_request == json.loads(rv.data)
    assert rv.content_type == 'application/json'


def test_invalid_user_data_update_failure(client):
    """
    Used to test for invalid data in
    learner update
    :param client: Flask test client
    """
    rv = client.put('/api/v1.0/learners/student/update/udoyen',
                    data=json.dumps(SampleData.invalid_user_data_update_failure),
                    headers={"Content-Type": "application/json", "Accept": "application/json"})
    print(f"Response: {rv.data}")
    assert 400 == rv.status_code
    assert rv.content_type == 'application/json'


def test_delete_learner(client):
    """
    Used to test the delete method for
    learner
    :param client: Flask test client
    """
    rv = client.delete('/api/v1.0/learners/student/delete/udoyen')
    assert 200 == rv.status_code


def test_delete_non_existent_learner(client):
    """
    Used to test for the proper
    response to the addition of a
    non-existent user
    :param client: Flask test client
    """
    rv = client.delete('/api/v1.0/learners/student/delete/oyen')
    assert 400 == rv.status_code