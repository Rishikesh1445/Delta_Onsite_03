from flask import Blueprint, request, jsonify
from ..models import user,items
from .. import db

newUser = Blueprint('newUser', __name__)

@newUser.route('/newUser', methods=['POST'])
def addUser():
    data = request.get_json()
    newUser = user(name = data['name'] , balance = 0)
    db.session.add(newUser)
    db.session.commit()

    return jsonify({"message" : "Registered Successfully"}), 200