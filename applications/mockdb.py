# test mock  request twice, response same
from flask import Blueprint
from flask import jsonify

from Register.register_db import add_instance
from Register.register_db import db
from Register.register_db import get_all

bp_cat = Blueprint('cat', __name__, url_prefix='/cat')


class Cats(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    breed = db.Column(db.String(100))


@bp_cat.route('/create', methods=['POST'])
def create_cat():
    data = {'name': 'cat1', 'price': 99999999, 'breed': 'breed1'}
    add_instance(Cats, **data)
    return jsonify(msg='create success')


@bp_cat.route('/all', methods=["GET"])
def get_cats():
    cats = get_all(Cats)
    return jsonify(count=len(cats))
