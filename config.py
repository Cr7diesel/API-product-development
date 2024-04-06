import os

from sqlalchemy.engine.url import URL


BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_ENV = os.environ.get("FLASK_ENV")
    DEBUG = os.environ.get("DEBUG")


class DevelopConfig(Config):
    DEBUG = True

    url_object = URL.create(
        "postgresql+psycopg2",
        username=os.environ.get("DB_USERNAME"),
        password=os.environ.get("DB_PASSWORD"),
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
    )

    SQLALCHEMY_DATABASE_URI = url_object


class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
