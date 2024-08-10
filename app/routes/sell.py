from flask import Blueprint, request, jsonify
from ..models import user,items
from .. import db

sell = Blueprint('sell', __name__)

@sell.route('/sell', methods=['POST'])
def selly():
    data = request.get_json()
    user_details = user.query.filter_by(name = data['name']).first()
    userid = user_details.id
    task_id = data['id']

    item = items.query.filter_by(id = task_id).first()

    if item.ownership == userid :
        item.sell = True
        db.session.commit()
        return jsonify({'message': 'Item sell status changed successfully'})
    else:
        return jsonify({'message': 'Not ur item mf'})