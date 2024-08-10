from flask import Blueprint, request, jsonify
from ..models import user,items
from .. import db
import random

coinss = Blueprint('coinss', __name__)

@coinss.route('/coins', methods=['GET'])
def coinssss():
    user_id = request.args.get('id')
    random_int = random.randint(1000, 5000)
    user_details = user.query.filter_by(id = user_id).first()
    user_details.balance = random_int + user_details.balance
    db.session.commit()

    return f'User {user_id}'