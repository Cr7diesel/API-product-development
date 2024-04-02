import os
from flask import Flask
from dotenv import load_dotenv


load_dotenv()


def create_app(config_type=os.environ.get('CONFIG_TYPE')):
    app = Flask(__name__)
    app.config.from_object(config_type)
    return app