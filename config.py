class BaseConfig(object):
    DEBUG = True
    APP_NAME = "zhihu_download"
    PORT = 9966


class DeployConfig(BaseConfig):
    DEBUG = False


class TestingConfig(BaseConfig):
    pass
