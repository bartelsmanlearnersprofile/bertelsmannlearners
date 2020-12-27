

class Config(object):
    '''
    Class used for configurations settings
    :arg object class
    '''
    # TODO: Enter this values in the environmental settings in the cloud

    import os

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_TRACK_MODE = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TESTING = False
    DEBUG = False


class DevelopmentConfig(Config):
    '''
    Class for flask development configurations
    :arg Config Main config class
    '''
    DEBUG = True


class TestingConfig(Config):
    """
    Class for flask testing configurations
    :arg Config Main config class
    """
    TESTING = True
