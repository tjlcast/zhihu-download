class BaseConfig(object):
    DEBUG = True
    APP_NAME = "fsdajklfjdsalk1654356"
    PORT = 5001


class DeployConfig(BaseConfig):
    DEBUG = False


class TestingConfig(BaseConfig):
    pass
