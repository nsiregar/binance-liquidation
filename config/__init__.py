import os
from functools import lru_cache

from config.development import DevelopmentConfig
from config.production import ProductionConfig
from config.test import TestConfig


@lru_cache(maxsize=None)
def get_config():
    app_env = os.getenv("APP_ENV", "development")
    config_factory = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "test": TestConfig,
    }
    app_config = config_factory.get(app_env, DevelopmentConfig)
    app_config.env = app_env
    return app_config


config = get_config()
