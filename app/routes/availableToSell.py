from flask import Blueprint, request, jsonify
from ..models import user,items
from .. import db

availableToSell = Blueprint('availableToSell', __name__)

@availableToSell.route('/availableToSell', methods=['POST'])
def sellList():
    data = request.get_json()
    user_details = user.query.filter_by(name = data['name']).first()
    userid = user_details.id

    all_items = items.query.filter((items.id == userid) & (items.sell == True)).all()

    json_list = []
    for item in all_items:
        itemy = item.to_dict()
        json_list.append(itemy)

    return jsonify(json_list), 200