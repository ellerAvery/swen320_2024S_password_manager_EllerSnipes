from decouple import config

class Config(object):
    DEBUG = False
    TESTING = True
    CSRF_ENABLED = True
    #SECRET_KEY = config("SECRET_KEY", default="guess-me")
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    EXHORT_PYTHON_VIRTUAL_ENV=True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False