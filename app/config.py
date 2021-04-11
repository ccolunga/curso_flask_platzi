class Config(object):
    SECRET_KEY = 'SUPER SECRET'
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
