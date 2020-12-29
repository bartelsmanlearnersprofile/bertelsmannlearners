from marshmallow import Schema, fields, pre_load, validate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Learner(db.Model, dict):
    """
    Model class for learners
    """
    __tablename__ = 'learners'
    id = db.Column(db.Integer, primary_key=True)
    slackname = db.Column(db.String(200), nullable=False)
    firstname = db.Column(db.String(200), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)

    def __init__(self, slackname, firstname, lastname):
        super().__init__()
        self.slackname = slackname
        self.firstname = firstname
        self.lastname = lastname


# Schema validations
class LearnerSchema(ma.Schema):
    class Meta:
        model = Learner
    id = fields.Integer()
    slackname = fields.String(required=True)
    firstname = fields.String(required=True)
    lastname = fields.String(required=True)

# INFO: How to use the schema
# author = Author(name="Chuck Paluhniuk")
# author_schema = AuthorSchema()
# book = Book(title="Fight Club", author=author)
# session.add(author)
# session.add(book)
# session.commit()
#
# dump_data = author_schema.dump(author)
# print(dump_data)
# {'id': 1, 'name': 'Chuck Paluhniuk', 'books': [1]}
#
# load_data = author_schema.load(dump_data, session=session)
# print(load_data)
# <Author(name='Chuck Paluhniuk')>


learner_schema = LearnerSchema()