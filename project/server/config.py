import os

basedir = os.path.abspath(os.path.dirname(__file__))

# config for Flask
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'prod'
    REDIS_URL = "redis://redis:6379/0"
