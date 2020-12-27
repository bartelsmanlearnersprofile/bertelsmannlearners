from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from FlaskAPI import app
from FlaskAPI.model import db

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
