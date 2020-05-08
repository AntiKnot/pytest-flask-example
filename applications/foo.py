from flask import Blueprint
from flask import jsonify

bp_foo = Blueprint('foo', __name__, url_prefix='/')


@bp_foo.route('/')
def hello_world():
    return 'Hello World!'


@bp_foo.route('/ping')
def ping():
    return jsonify(ping='pong')
