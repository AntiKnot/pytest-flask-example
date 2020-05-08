from applications.foo import bp_foo
from applications.mockdb import bp_cat
from applications.mockfolder import bp_file


def register_blueprints(app):
    app.register_blueprint(bp_foo)
    app.register_blueprint(bp_cat)
    app.register_blueprint(bp_file)
