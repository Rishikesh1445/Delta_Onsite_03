from flask import Blueprint, request, jsonify
from ..models import user,items
from .. import db

buy = Blueprint('buy', __name__)

@buy.route('/buy', methods=['POST'])
def buyy():
    data = request.json

    name = data['name']
    user_details = user.query.filter_by(name = data['name']).first()
    userid = user_details.id

    task_id = data['id']
    item = items.query.filter_by(id = task_id).first()
    uploaded_user = user.query.filter_by(id = item.ownership).first()

    if item.ownership != userid :
        if item.sell == True:
            if item.price < user_details.balance:
                user_details.balance = user_details.balance - item.price
                uploaded_user.balance = user_details.balance + item.price
                item.ownership = user_details.id
                item.sell = False
                db.session.commit()
            else:
                return jsonify({'message': 'Insufficient balance'}), 400
        else:
            return jsonify({'message': 'Not for sale'}), 400
    else:
        return jsonify({'message': 'This is your item'}), 400