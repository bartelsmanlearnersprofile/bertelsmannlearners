"""
This script runs the FlaskAPI application
"""

from os import environ
from FlaskAPI import app
from FlaskAPI.model import db, ma
import config

if __name__ == '__main__':
    app.config.from_object("config.Config")
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '3000'))
    except ValueError:
        PORT = 3000
    app.run(HOST, PORT, debug=True)
