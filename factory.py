from flask import Flask

from Register.register_blueprint import register_blueprints
from Register.register_db import db
from Register.register_login import login_manager


def create_app(cf):
    app = Flask(__name__)
    app.config.from_object(cf)
    app.app_context().push()
    register_blueprints(app)
    db.init_app(app)
    login_manager.init_app(app)
    return app
