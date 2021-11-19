import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Class with configuration parameters for Flask
    """

    DEBUG = False
    TESTING = False
    SECRET_KEY = 'prod'
    REDIS_URL = "redis://redis:6379/0"
