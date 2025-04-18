from flask import Flask
from flask_jwt_extended import JWTManager

import models  # noqa: F401
from instance.database import init_db

# Import routes
from route.index import index_router
from route.user import user_router


def create_app(config_module="config.local"):
    app = Flask(__name__)
    app.config.from_object(config_module)
    init_db(app)

    # Initialize JWTManager
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(index_router)
    app.register_blueprint(user_router)

    return app
