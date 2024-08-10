from flask import Blueprint, request, jsonify
from ..models import user,items
from .. import db
import random

createItem = Blueprint('createItem', __name__)

@createItem.route('/createItem', methods=['POST'])
def itemCreate():
    data = request.get_json()
    random_int = random.randint(1000, 5000)
    
    user_details = user.query.filter_by(name = data['name']).first()
    userid = user_details.id

    new_item = items(name = data['item'], price = random_int, ownership = userid )

    db.session.add(new_item)
    db.session.commit()

    return jsonify({"message" : "Registered Successfully"}), 200