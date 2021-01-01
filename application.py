"""
This script runs the FlaskAPI application
"""

from os import environ

from FlaskAPI import app as application
from FlaskAPI.model import db, ma

if __name__ == '__main__':
    application.config.from_object("config.Config")
    with application.app_context():
        db.init_app(application)
        ma.init_app(application)
        db.create_all()
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '3000'))
    except ValueError:
        PORT = 3000
    application.run('0.0.0.0', PORT, debug=False)
