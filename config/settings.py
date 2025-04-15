from flask import Flask
from route.index import index_router


def create_app(config_module="config.local"):
    app = Flask(__name__)
    app.config.from_object(config_module)
    app.register_blueprint(index_router)
    return app
