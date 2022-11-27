##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
