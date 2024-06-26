import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


load_dotenv()

database = SQLAlchemy()
db_migration = Migrate()


def create_app(config_type=os.environ.get("CONFIG_TYPE")):
    app = Flask(__name__)
    app.config.from_object(config_type)
    initialize_extensions(app)
    return app


def initialize_extensions(app):
    database.init_app(app)
    db_migration.init_app(app, database)

    import core.models #noqa 
